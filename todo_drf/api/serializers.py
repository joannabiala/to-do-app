



















#----------------------------------------------
# from rest_framework import serializers
# from .models import Task
# from api.models import Account
#
#
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = Account
#         fields = ['email', 'username', 'password', 'password2']
#
#     def save(self):
#         account = Account(
#             email = self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationErrir({'password': 'Passwords must match!'})
#         account.set_password(password)
#         account.save()
#         return account
