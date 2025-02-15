from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_desc', 'date_created', 'completed', 'image']
        image = serializers.ImageField(max_length=None, use_url=True)


class UserSerializers(serializers.ModelSerializer):
    password = Serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.created(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class Meta:
    model = get_user_model()
    fields = ('username', 'password')
