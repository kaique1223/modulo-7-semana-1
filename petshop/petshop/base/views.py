from django.shortcuts import render
from django.http import HttpResponse
from base.forms import contatoform


def inicio(request):
    
    return render(request,'inicio.html')

def contato(request):
    sucesso = False

   
    form = contatoform(request.POST)
    if form.is_valid():
        sucesso = True
        form.save()
         
            

    contexto = {
        'telefone' : '(99)99999.9999',
        'responsavel' : 'MARIA ',
        'form': form,
        'sucesso': sucesso
        
        }
   
    return render(request,'contato.html',contexto)
