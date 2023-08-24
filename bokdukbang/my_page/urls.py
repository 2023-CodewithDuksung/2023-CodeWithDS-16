from django.urls import path
from .views import *

app_name = "my_page"

urlpatterns = [
    path("", MyProfile.as_view(), name="my_profile"),
    path("modify/", MyProfilePut.as_view(), name="my_profile_put"),
    path("my-find-rooms/", MyFindRoomList.as_view(), name="my_find_room_list"),
    path("my-offer-rooms/", MyOfferRoomList.as_view(), name="my_offer_room_list"),
    path("my-promotion-rooms/", MyPromotionRoomList.as_view(), name="my_promotion_room_list"),
    path("my-interest/", MyInterestList.as_view(), name="my_interest_list")
]
