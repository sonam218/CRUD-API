from rest_framework import serializers
from students import models
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        # fields = ['id', 'std_name', 'std_class', 'mobile_number', 'image', 'address']
        # exclude = ['address']
        read_only_fields = ['id']