from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT'])
def hello_word(request):
    if request.method == "POST":
        name  = request.data.get('name')
        age = request.data.get('age')
        return Response({'menssagem':f"ola,{name} seja bem vindo!,voce tem {age} anos"})
        

    return Response({
        'whatsszap':'44-974008114',
        'menssagem':'helo_word'})
