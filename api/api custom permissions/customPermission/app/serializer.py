from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

    def validat_roll(self, value):
        if value<100:
            raise serializers.ValidationError("Your roll must be greater then 100")
        return value