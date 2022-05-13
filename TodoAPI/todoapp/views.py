from django.shortcuts import render

from todoapp.serializers import TodoSerializers
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from todoapp.models import Todo

# Create your views here.
#This APIView will get all the todo items
class GetTodoView(APIView):
    #instantiating serializer
    serializer_class = TodoSerializers
    #Providing permission so that only authenticated user can access data
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # data = Todo.objects.(user=request.user)
        data = Todo.objects.all()
        #we get the serialized data by providing data to the serializer class
        #it serialize only one instance to achieve multiple instance use many=True
        serializer = self.serializer_class(data, many=True)
        #extract the data from the serializer by using data attribute to get the data
        serialized_data = serializer.data
        # Return the serailized data as response to the API get request 
        return Response(serialized_data)

#This APIView will create todo items
class CreateTodoView(APIView):
    #instantiating serializer
    serializer_class = TodoSerializers
    #Providing permission so that only authenticated user can access data
    # permission_classes = [IsAuthenticated,IsAdminUser]

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data, context = {'request':request})
        #Checking the validity of an serializer and saving it if valid
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            #Return response to the Post API request
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serialized_data, status=status.HTTP_400_BAD_REQUEST)

#This APIView will return single todo depend on primary key provided
#In this APIView you can get, update and delete todo
#Only accessible to the admin user
class TodoDetailView(APIView):
    #instantiating serializer
    serializer_class = TodoSerializers
    #Providing permission so that only authenticated user can access data
    permission_classes = [IsAuthenticated,IsAdminUser]

    #Using this function to get correct object using primary
    #Return object if found else Error
    def get_object(self, pk):
        try:
            obj = Todo.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Todo.DoesNotExist:
            raise Http404

    #get particular item from the list
    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status = status.HTTP_200_OK)

    #get particular item from the list and can update it.
    def put(self, request, pk, format=None):
        tododata = self.get_object(pk)
        serializer = self.serializer_class(tododata, data=request.data, context= {'request':request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.Http_400_BAD_REQUEST)
        
    #delete an item.
    def delete(self, request, pk, format=None):
        tododata = self.get_object(pk)
        tododata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
