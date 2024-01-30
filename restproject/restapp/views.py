from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def FirstGet(request):
    if request.method == 'GET':
        return Response({'message':'My first get request'})

@api_view(['POST'])
def FirstPost(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        print(['name'])
        return Response({'message':'My first post request'})

@api_view(['POST'])
def test(request):
    if request.method == 'POST':
        aloowedLevel = ['B3','B4']
        data = request.data
        if int(data["age"]) >= 25 and data['language'] in aloowedLevel:
            return Response({"message":f"{data['name']} подходит"})
        else:
            return Response({"message":f"{data['name']} не подходит"})
