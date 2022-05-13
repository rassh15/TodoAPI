from email.policy import default
import imp
from rest_framework import serializers
from todo.models import Todo

'''
Here we use serializers to convert the model data into 
python datatypes. 
That later can easily be rendered into json data.
We inherit serializers of ModelSerializer class.

'''

class TodoSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        #Model class from the model.py
        model = Todo
        #To get the all field from the model
        fields = '__all__'