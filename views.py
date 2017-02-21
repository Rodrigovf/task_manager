from django.shortcuts import render
from django.http import HttpResponse
def tarefa(request,ano,mes):
	return HttpResponse("tarefa/"+str(ano+"/"+mes))	
		
class Tarefa(object):
	def __init__(self, titulo, data):
		self.titulo = titulo
		self.data = data
	
	def __stsr__(self):
		return self.titulo