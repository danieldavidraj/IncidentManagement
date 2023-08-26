from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from forms import IncidentForm
from models import Incident
from rest_framework.response import Response

import pickle
import keras
from keras_preprocessing.sequence import pad_sequences
import numpy as np

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def collect(request, format=None):
    user = request.user
    form = IncidentForm(request.POST)
    if form.is_valid():
        instance = Incident(user=user, message=form.cleaned_data['message'])
        instance.save()

        # ML model invocation

        with open('tokenizer.pickle', 'rb') as handle:
            loaded_tokenizer = pickle.load(handle)

        with open('label_encoder.pickle', 'rb') as handle:
            loaded_label_encoder = pickle.load(handle)

        loaded_model = keras.models.load_model('issue_classification_model.h5')
        new_issue = ["Application keeps loading"]
        new_issue_seq = loaded_tokenizer.texts_to_sequences(new_issue)

        new_issue_seq = pad_sequences(new_issue_seq, maxlen=100)
        predict_x=loaded_model.predict(new_issue_seq) 
        classes_x=np.argmax(predict_x,axis=1)
        predicted_class_label = loaded_label_encoder.inverse_transform(classes_x)
        user_response = predicted_class_label[0]

        return Response({'message': user_response}, status=200)
    else:
        return Response({'message': 'Invalid post data'}, status=400)
