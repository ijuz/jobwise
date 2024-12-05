from rest_framework.exceptions import ValidationError # type: ignore
from rest_framework import serializers # type: ignore
from .models import CustomUser,UserProfile


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields =['id','username','email','password','phone_number']

    def validate_username(self,value):
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Username already exists.")
        return value
    
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value).exists():
            raise  ValidationError("Email already exists.")
        return value
    
    def validate_phone_number(self,value):
        if CustomUser.objects.filter(phone_number=value).exists():
            raise  ValidationError("Phone Number already exists.")
        return value
        
    def create(self,validated_data):
        user = CustomUser(
            username = validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()

        UserProfile.objects.create(user=user)

        return user


class WrokerprofileSerializer(serializers.ModelSerializer):
    user = SignupSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields =['user','full_name','age']