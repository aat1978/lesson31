from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserSerializer, UserDetailSerializer, UserListSerializer, LocationSerializer, \
    UserCreateSerializer


class UserPagination(PageNumberPagination):
    page_size = 4


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserDeleteView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
