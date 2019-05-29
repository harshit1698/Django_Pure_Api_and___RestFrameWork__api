from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings

from rest.models import Ap


User=get_user_model()
jwt_payload_handler=api_settings.JWT_PAYLOAD_HANDLER
jwt_encode=api_settings.JWT_ENCODE_HANDLER



class RegisterUserSerializer(ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    token=serializers.SerializerMethodField()
    is_staff= serializers.SerializerMethodField()

    class Meta:
        model= User
        fields=[
            'username',
            'email',
            'is_staff',
            'password',
            'password2',
            'token'
        ]

    def get_token(self,obj):
        user=obj
        payload = jwt_payload_handler(user)
        token = jwt_encode(payload)
        return token

    def get_is_staff(self,obj):
        obj.is_staff=True
        return True

    def validate(self, attrs):
        pw=attrs.get('password')
        p2=attrs.pop('password2')
        if pw != p2:
            raise serializers.ValidationError("Password must match")
        return attrs

    def create(self, validated_data):
        user_obj=User(username=validated_data.get('username'),email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj


class UserSerializer(ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']


class ApSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ap
        fields = ['user','name','age','image','uri']
        read_only_fields = ['user']

    def get_uri(self,obj):
        return "http://127.0.0.1:8000/rest/gett/{id}".format(id=obj.id)


    # def validate(self,attrs):
    #     x=attrs.get("name")
    #     if len(x) > 20:
    #         raise ValidationError("Name should be greater than 20")
    #     return attrs
    #
    # def create(self, validated_data):
    #     name = validated_data.get("name",None)
    #     if len(name) < 5:
    #         raise ValidationError("Name Is Too short")
    #     else:
    #         return validated_data

    def validate_name(self,attrs):
        name = attrs
        if len(name) < 5:
            raise ValidationError("Nope Sorry Bro")
        else:
            return attrs




