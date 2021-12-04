from typing import Any

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from Articles.models import ArticleComment, LandingPageArticles
from ProductApp.models import MainProductDatabase
from Profile.models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'first_name': {"required": False, "allow_null": True},
            'last_name': {"required": False, "allow_null": True},
            'email': {"required": False, "allow_null": True},
        }

    def create(self, validated_data) -> User:
        """ Create User serializer """

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data) -> User:

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"

    def update(self, instance, validated_data) -> Profile:

        password = validated_data
        print(password)

        profile = super().update(instance, validated_data)
        
        print('jestem za profile')
        
        for key, value in validated_data.items():
            if key != 'user':
                if key == 'keep_me':
                    try:
                        profile.keep_me = value
                    except:
                        pass
                else:
                    try:
                        profile.newsletter = value
                    except:
                        pass

        # if password:
        #     user.set_password(password)
        #     user.save()

        return profile


class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for token creation """
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    email = serializers.CharField(required=False)


    def validate(self, attrs) -> Any:
        email = attrs.get('email')
        password = attrs.get('password')
        username = attrs.get('username')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            username=username,
            password= password
        )

        if not user:
            message = _('Unable to authenticate')
            raise serializers.ValidationError(message, code='authentication')

        attrs['user'] = user

        return attrs

class BlogArticlesSerializer(serializers.ModelSerializer):
    """ Blog comments section Serializer  """

    new_fields = serializers.SerializerMethodField('get_data_from_comment')

    class Meta:
        model = ArticleComment
        fields = ('name', 'comment', 'email', 'article', 'new_fields', 'parent')

    def create(self, validated_data):
        """ Create blog comment serializer """

        comment = ArticleComment.objects.create(**validated_data)

        return comment

    def get_data_from_comment(self, article):
        print(article.__dict__)
        return {
            'id': article.id,
            'publish': article.publish,
            'level': article.level
        }

class ProductSerializer(serializers.ModelSerializer):
    """ Get products data Serializer  """

    class Meta:
        model = MainProductDatabase
        fields = '__all__'
