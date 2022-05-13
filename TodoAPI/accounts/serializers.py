import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Using Django User Model
User = get_user_model()

#User Registration Form serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only = True)
    password2 = serializers.CharField(required=True, write_only = True)

     
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2',
            'is_staff',
            'is_active',
        ]
        extra_kwargs = {
            'password' : {'write_only':True},
            'password2' : {'write_only':True},
        }

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username  = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')
        is_staff = validated_data.get('is_staff')
        is_active = validated_data.get('is_active')

        if password == password2:
            user = User(username=username, email = email)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = is_staff
            user.is_active = is_active
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {
                    'error':'Both passwords do not match'
                }
            )


#Using serializer to obtain custom response
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data to include
        data.update({'First Name': self.user.first_name})
        data.update({'Last Name': self.user.last_name})
        data.update({'Email': self.user.email})
        data.update({'IsStaff': self.user.is_staff})
        data.update({'IsActive': self.user.is_active})
        # and everything  send in the response
        return data







