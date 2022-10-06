import uuid

from rest_framework import serializers

from shortener.models import Url


class UrlCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("link",)

    def create(self, validated_data):
        url = Url.objects.create(
            link=validated_data["link"],
            short_link=str(uuid.uuid4())[:5],
            user=self.context.get("request").user,
        )
        url.save()
        return url


class UrlGetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("id", "link", "short_link")


class UrlDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"
