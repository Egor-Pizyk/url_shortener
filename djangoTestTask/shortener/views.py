from django.shortcuts import redirect
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from shortener.models import Url
from shortener.serializers import (
    UrlCreateSerializer,
    UrlGetListSerializer,
    UrlDetailSerializer,
)


class CreateLinkAPI(CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlCreateSerializer
    permission_classes = (IsAuthenticated | IsAdminUser,)


class UrlsListAPI(ListAPIView):
    model = Url
    serializer_class = UrlGetListSerializer
    permission_classes = (IsAuthenticated | IsAdminUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.model.objects.all()
        return self.model.objects.filter(user=user)


class UrlDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = UrlDetailSerializer
    permission_classes = (IsAuthenticated | IsAdminUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Url.objects.all()
        return Url.objects.filter(user=user)


def url_redirect(request, short_link):
    url = Url.objects.get(short_link=short_link)
    url.counter += 1
    url.save()
    return redirect(url.link)
