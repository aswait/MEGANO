from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Avatar, Profile


class AvatarSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Avatar
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url

    # def update(self, instance, validated_data):
    #     instance.crc = validated_data.get("src", instance.src)
    #     instance.alt = validated_data.get("alt", instance.alt)
    #     instance.save()
    #     return instance


class ProfileSerializer(serializers.ModelSerializer):
    avatar = AvatarSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "fullName",
            "phone",
            "email",
            "avatar",
        ]

    def update(self, instance, validated_data):
        instance.fullName = validated_data.get("fullName", instance.fullName)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()
        return instance


class PasswordSerializer(serializers.ModelSerializer):
    currentPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "currentPassword",
            "newPassword",
        ]
