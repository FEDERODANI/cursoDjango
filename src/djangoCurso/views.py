from django.views.generic import TemplateView
from django.shortcuts import render


def index(request):
	""" vista basado en funciones"""
	return render(request, 'index.html', {})


class IndexView(TemplateView):
	""" vista basado en clases"""
    template_name = "index.html"