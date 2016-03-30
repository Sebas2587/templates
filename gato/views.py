from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Gato

# Create your views here.

def gato(request):
	gatos = Gato.objects.order_by('id')
	template = loader.get_template('gato.html')
	title = 'gatitos pag'

	context = {
		'gato': gatos,
		'title': title,

	}
	return HttpResponse(template.render(context, request))


def saludo(request):
	template = loader.get_template('saludo.html')
	big_title = 'encabezado de la pagina'
	title = 'aqui no hay gatos'
	context = {
		'big_title': big_title,
		'title': title
	}

	return HttpResponse(template.render(context, request))