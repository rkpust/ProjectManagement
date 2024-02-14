from .models import *
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'note', 'status', 'manager']