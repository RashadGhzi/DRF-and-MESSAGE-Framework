from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    def validate_roll(self, value):
        if value < 100:
            raise serializers.ValidationError("Roll must be greater then 100")
        return value

    def validate(self, attrs):
        name = attrs.get('name')
        city = attrs.get('city')
        if name == 'Amir' and city != 'Mumbai':
            raise serializers.ValidationError("If name is Amir then city must be Mumbai.")
        return attrs