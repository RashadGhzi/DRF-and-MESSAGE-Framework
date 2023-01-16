from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with r')
        return value
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    # Field Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    # Object Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower()=='rahul' and city.lower()!='dhaka':
            raise serializers.ValidationError('Your city should be Dhaka')
        return data

        
    
