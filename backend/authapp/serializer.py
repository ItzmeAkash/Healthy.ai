from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6,write_only=True)
    
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','password')  
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
        
        
        # Validation
        
        
        def create(self, validate_data):
            password = validate_data.pop('password', None)
            if password:
                # If password is match, set the hased password
                user = super().create(validate_data=validate_data)
                user.set_password(password)
                user.save()
                return user
            raise serializers.ValidationError("Password do not match or missing")
        
        def to_internal_value(self, data):
            data = super().to_internal_value(data)
            errors = {}

            for field, value in data.items():
                if value == '':
                    errors[field] = "This field is required."

            if errors:
                raise serializers.ValidationError(errors)

            return data