





























#---------------------------------------
# from django.shortcuts import render
# from django.http import JsonResponse
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import TaskSerializer, RegistrationSerializer
#
# from .models import Task
#
#
# # Create your views here.
#
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/task-list/',
#         'Detail View': '/task-detail/<str:pk>/',
#         'Create': '/task-create/',
#         'Update': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<str:pk>/',
#         'User create': '/register/'
#     }
#
#     return Response(api_urls)
#
#
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all().order_by('-id')
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = TaskSerializer(tasks, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['PUT'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#
#     return Response('Item succsesfully delete!')
#
#
# @api_view(['POST'])
# def registration_view(request):
#
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data = request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = "succsessfully registered new user"
#             data['email'] = account.email
#             data['username'] = account.username
#
#         return Response(data)
#     else:
#         data = serializer.errors
#         return Response(data)
#



