from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView
from manager.models import Room, TimeSlot, AdvanceBooking
from accounts.models import User
from .serializers import RoomSerializer, TimeSlotSerializer, BookSerializer, CancelSerializer, AdvanceBookingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from customer.models import TimeSlotBook, TimeSlotCancel
from .permissions import IsManager
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, IsManager)

    def perform_create(self, serializer):
        serializer.save(room_owner=User.objects.get(id=self.request.user.id))

class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, IsManager)
 
    def get_queryset(self, **kwargs):
        return Room.objects.filter(room_owner=User.objects.get(id=self.request.user.id))

class RoomDetailAPIView(RetrieveAPIView):
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, IsManager)

    def get_queryset(self, **kwargs):
        return Room.objects.filter(room_owner=User.objects.get(id=self.request.user.id))

class RoomDeleteAPIView(DestroyAPIView):
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return Room.objects.filter(room_owner=User.objects.get(id=self.request.user.id))


# Time Slot API Views
class TimeSlotCreateAPIView(CreateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def perform_create(self, serializer):
        serializer.save(time_slot_owner=User.objects.get(id=self.request.user.id), room_id=Room.objects.get(id=self.kwargs['room_id']))

class TimeSlotListAPIView(ListAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsManager, )
 
    def get_queryset(self, **kwargs):
        return TimeSlot.objects.filter(time_slot_owner=User.objects.get(id=self.request.user.id), room_id=Room.objects.get(id=self.kwargs['pk']))

class TimeSlotDetailAPIView(RetrieveAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return TimeSlot.objects.filter(time_slot_owner=User.objects.get(id=self.request.user.id), room_id=Room.objects.get(id=self.kwargs['room_id']))

class TimeSlotUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return TimeSlot.objects.filter(time_slot_owner=User.objects.get(id=self.request.user.id))


class TimeSlotDeleteAPIView(DestroyAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return TimeSlot.objects.filter(time_slot_owner=User.objects.get(id=self.request.user.id))


# Booked Time Slot History, Manager'
class BookTimeSlotAPIView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return TimeSlotBook.objects.filter(manager_id=User.objects.get(id=self.request.user.id))

class CancelTimeSlotAPIView(ListAPIView):
    serializer_class = CancelSerializer
    permission_classes = (IsAuthenticated, IsManager, )

    def get_queryset(self, **kwargs):
        return TimeSlotCancel.objects.filter(manager_id=User.objects.get(id=self.request.user.id))


class EditAdvanceDayAPIView(APIView):
    permission_classes = (IsAuthenticated, IsManager)

    def post(self, request):
        serializer = request.data
        no_of_days = serializer.get('no_of_days', None)
        user = AdvanceBooking.objects.get(manager_id=request.user)
        user.no_of_days = no_of_days
        user.save()
        return Response({"message": "Updated Successfully."}, status=status.HTTP_200_OK)