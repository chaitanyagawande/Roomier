from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from manager.models import TimeSlot, Room
from accounts.models import User
from .serializers import TimeSlotSerializer, BookTimeSlotSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsCustomer
from customer.models import TimeSlotBook, TimeSlotCancel
from .serializers import BookSerializer, CancelTimeSlotSerializer

class SearchAPIView(ListAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = (IsAuthenticated, IsCustomer)
    
    def get_queryset(self, **kwargs):
        date = self.request.query_params.get("date")
        start_time = self.request.query_params.get("start_time")
        end_time = self.request.query_params.get("end_time")
        print(date)
        return TimeSlot.objects.filter(start_time=start_time, end_time=end_time)


class BookTimeSlotAPIView(CreateAPIView):
    queryset = TimeSlotBook.objects.all()
    serializer_class = BookTimeSlotSerializer
    permission_classes = (IsAuthenticated, IsCustomer, )

    def perform_create(self, serializer):
        manager_id = self.request.POST["manager_id"]
        date = self.request.POST["date"]
        start_time = self.request.POST["start_time"]
        end_time = self.request.POST["end_time"]
        room_id = self.request.POST["room_id"]
        serializer.save(customer_id=User.objects.get(id=self.request.user.id), manager_id=User.objects.get(id=manager_id), date=date, start_time=start_time, end_time=end_time,room_id=Room.objects.get(id=room_id))


class CancelTimeSlotAPIView(CreateAPIView):
    queryset = TimeSlotCancel.objects.all()
    serializer_class = CancelTimeSlotSerializer
    permission_classes = (IsAuthenticated, IsCustomer, )

    def perform_create(self, serializer):
        manager_id = self.request.POST["manager_id"]
        date = self.request.POST["date"]
        start_time = self.request.POST["start_time"]
        end_time = self.request.POST["end_time"]
        room_id = self.request.POST["room_id"]
        (TimeSlotBook.objects.get(customer_id=User.objects.get(id=self.request.user.id), manager_id=User.objects.get(id=manager_id), date=date, start_time=start_time, end_time=end_time,room_id=Room.objects.get(id=room_id)).delete())
        serializer.save(customer_id=User.objects.get(id=self.request.user.id), manager_id=User.objects.get(id=manager_id), date=date, start_time=start_time, end_time=end_time,room_id=Room.objects.get(id=room_id))


class BookedTimeSlotAPIView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsCustomer, )

    def get_queryset(self, **kwargs):
        return TimeSlotBook.objects.filter(customer_id=User.objects.get(id=self.request.user.id))


class CancelledTimeSlotAPIView(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsCustomer, )

    def get_queryset(self, **kwargs):
        return TimeSlotCancel.objects.filter(customer_id=User.objects.get(id=self.request.user.id))
