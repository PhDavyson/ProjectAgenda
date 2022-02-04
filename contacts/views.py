from django.shortcuts import render
from .models import Contact


def index(request):
    contatos = Contact.objects.all()
    return render(request, 'contacts/index.html', {
        'contatos': contatos
    })


def acessar_contato(request, contato_id):
    contato = Contact.objects.get(id=contato_id)
    return render(request, 'contacts/acessar_contato.html', {
        'contato': contato
    })

