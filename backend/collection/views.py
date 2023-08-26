from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import IncidentForm
from .models import Incident
from rest_framework.response import Response

import pickle
import keras
from keras.preprocessing.sequence import pad_sequences
import numpy as np

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_incidents_for_user(request, format=None):
    user = request.user
    incidents = Incident.objects.filter(user=user)
    return Response({'incidents': incidents}, status=200)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def collect_incident_for_user(request, format=None):
    user = request.user
    form = IncidentForm(request.data)
    if form.is_valid():
        message = form.cleaned_data['message']

        # ML model invocation

        with open('models/tokenizer.pickle', 'rb') as handle:
            loaded_tokenizer = pickle.load(handle)

        with open('models/label_encoder.pickle', 'rb') as handle:
            loaded_label_encoder = pickle.load(handle)

        loaded_model = keras.models.load_model('models/issue_classification_model.h5')
        new_issue = [message]
        new_issue_seq = loaded_tokenizer.texts_to_sequences(new_issue)

        new_issue_seq = pad_sequences(new_issue_seq, maxlen=100)
        predict_x=loaded_model.predict(new_issue_seq) 
        classes_x=np.argmax(predict_x,axis=1)
        predicted_class_label = loaded_label_encoder.inverse_transform(classes_x)
        user_response = predicted_class_label[0]

        instance = Incident(user=user, message=message, resolution=user_response)
        instance.save()

        return Response({'message': user_response}, status=200)
    else:
        return Response({'message': 'Invalid form data'}, status=400)
