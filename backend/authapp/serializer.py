from rest_framework import serializers
from .models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    # confirmpassword = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','password')  
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
        
        
        # Validation
        # def validate(self,data):
        #     if data['password']!= data.pop('confirmpassword'):
        #         raise serializers.ValidationError("Pasword do not Match")
        #     return data
        
        def create(self, validate_data):
            password = validate_data.pop('password', None)
            if password:
                # If password is match, set the hased password
                user = User.objects.create_user(**validate_data)
                user.set_password(password)
                user.save()
                return user
            raise serializers.ValidationError("Password do not match or missing")