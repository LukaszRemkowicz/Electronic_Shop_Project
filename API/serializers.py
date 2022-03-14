from typing import Any
from os import error

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from Articles.models import ArticleComment, LandingPageArticles
from ProductApp.models import MainProductDatabase
from Profile.models import User
from Emails.models import Newsletter
from ProductApp.models import Phones


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("password", "email", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
            "first_name": {"required": False, "allow_null": True},
            "last_name": {"required": False, "allow_null": True},
            "email": {"required": False, "allow_null": True},
        }

    def create(self, validated_data) -> User:
        """Create User serializer"""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data) -> User:
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data) -> User:

        # password = validated_data

        profile = super().update(instance, validated_data)

        for key, value in validated_data.items():
            if key != "user":
                if key == "keep_me":
                    try:
                        profile.keep_me = value
                    except error:
                        pass
                else:
                    try:
                        profile.newsletter = value
                    except error:
                        pass

        # if password:
        #     user.set_password(password)
        #     user.save()

        return profile


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for token creation"""

    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )
    email = serializers.CharField(required=False)

    def validate(self, attrs) -> Any:
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )

        if not user:
            message = _("Unable to authenticate")
            raise serializers.ValidationError(message, code="authentication")

        attrs["user"] = user

        return attrs


class BlogArticlesSerializer(serializers.ModelSerializer):
    """Blog comments section Serializer"""

    new_fields = serializers.SerializerMethodField("get_data_from_comment")

    class Meta:
        model = ArticleComment
        fields = ("name", "comment", "email", "article", "new_fields", "parent")

    def create(self, validated_data):
        """Create blog comment serializer"""

        comment = ArticleComment.objects.create(**validated_data)

        return comment

    def get_data_from_comment(self, article):
        return {"id": article.id, "publish": article.publish, "level": article.level}


class ProductSerializer(serializers.ModelSerializer):
    """Get products data Serializer"""

    class Meta:
        model = MainProductDatabase
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["email"]

    def create(self, validated_data):
        """Create blog comment serializer"""

        email = Newsletter.objects.filter(email=validated_data["email"])

        if len(email) == 0:

            newsletter = Newsletter.objects.create(**validated_data)
        else:
            newsletter = Newsletter.objects.filter(**validated_data)[0]

        return newsletter

    def to_representation(self, instance):
        return {"response": "Email has been added"}


class GetQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProductDatabase
        fields = ["id"]


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = "__all__"


class RetrievProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPageArticles
        fields = "__all__"
