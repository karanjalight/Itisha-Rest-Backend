from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class drinksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = itisha_drinks
        fields = ['drink_slug', 'drink_name', 'drink_type', 'drink_qty', 'drink_price', 'drink_description' ,'top_rated', 'recommended', 'offers']

class alcoholSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = alcohol_drinks
        fields = ['drink_slug','drink_type', 'drink_name', 'drink_qty', 'drink_price', 'drink_description', 'top_rated', 'recommended', 'offers']