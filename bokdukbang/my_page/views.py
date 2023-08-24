from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyInterest
from .serializers import MyInterestSerializer
from rooms_posts.models import Rooms
from rooms_posts.serializers import RoomsSerializer
from datetime import timedelta
from django.utils import timezone

# Create your views here.
class MyInterestList(APIView):
    def get(self, request):
        user_id = request.GET.get('user')

        interest = MyInterest.objects.filter(muser=user_id)
        serializer = MyInterestSerializer(interest, many=True)

        '''
        rooms = Rooms.objects.filter(rooms_id = interest.studio)
        serializer = RoomsSerializer(rooms)
        '''

        return Response(serializer.data)

