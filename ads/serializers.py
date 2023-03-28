from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from users.models import User


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    address = SerializerMethodField()

    def get_address(self, ad):
        return ad.author.location.name

    class Meta:
        model = Ad
        fields = "__all__"


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super.create(validated_data)

    class Meta:
        model = Selection
        fields = ["name", "items"]
