from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from typing import Any


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}, 'first_name': {"required": False, "allow_null": True},
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