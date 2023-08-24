from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyInterest
from .serializers import MyInterestSerializer
from rooms_posts.models import Rooms
from rooms_posts.serializers import RoomsSerializer
from accounts.models import User
from accounts.serializers import UserSerializer
from datetime import timedelta
from django.utils import timezone

# 마이페이지 내 정보 조회
class MyProfile(APIView):
    def get(self, request):
        user_id = request.GET.get('user')

        try:
            prof = User.objects.get(user_id=user_id)
            serializer = UserSerializer(prof)

            return Response(serializer.data)
        except:
            return Response({'message': "User not found"})

# 마이페이지 수정     
class MyProfilePut(APIView):

    def put(self, request):
        user_id = request.GET.get('user')
        try:
            prof = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(prof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyFindRoomList(APIView):

    def get(self, request):
        user_id = request.GET.get('user')

        try:
            find_rooms = Rooms.objects.filter(ruser=user_id, category="방 구하기")
        except Rooms.DoesNotExist:
            return Response({"message": "방 구하기 글을 올리지 않았습니다"}, status=status.HTTP_404_NOT_FOUND)
        
class MyOfferRoomList(APIView):

    def get(self, request):
        user_id = request.GET.get('user')

        try:
            find_rooms = Rooms.objects.filter(ruser=user_id, category="방 내놓기")
        except Rooms.DoesNotExist:
            return Response({"message": "방 내놓기 글을 올리지 않았습니다"}, status=status.HTTP_404_NOT_FOUND)
        
class MyPromotionRoomList(APIView):

    def get(self, request):
        user_id = request.GET.get('user')

        try:
            find_rooms = Rooms.objects.filter(ruser=user_id, category="방 홍보")
        except Rooms.DoesNotExist:
            return Response({"message": "방 홍보 글을 올리지 않았습니다"}, status=status.HTTP_404_NOT_FOUND)
        

# 내가 관심 누른 글 목록 조회
class MyInterestList(APIView):
    def get(self, request):
        user_id = request.GET.get('user')

        try:
            interest = MyInterest.objects.filter(muser=user_id)
            serializer = MyInterestSerializer(interest, many=True)

            '''
            rooms = Rooms.objects.filter(rooms_id = interest.studio)
            serializer = RoomsSerializer(rooms)
            '''
            return Response(serializer.data)
        except:
            return Response({"message": "This user has no interesting posts"})

        

