from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from forms import IncidentForm
from models import Incident
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def collect(request, format=None):
    user = request.user
    form = IncidentForm(request.POST)
    if form.is_valid():
        instance = Incident(user=user, message=form.cleaned_data['message'])
        instance.save()
        return Response({'message': 'Success'}, status=200)
    else:
        return Response({'message': 'Invalid post data'}, status=400)
