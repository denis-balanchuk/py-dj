# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Віталій',
		 'last_name': u'Подоба',
		 'ticket': 2123,	
		 'image': 'img/podoba.png'},
		{'id': 2,
		 'first_name': u'Денис',
		 'last_name': u'Баланчук',
		 'ticket': 254,	
		 'image': 'img/balanchuk.jpg'},
		{'id': 3,
		 'first_name': u'Денис',
		 'last_name': u'Борисов',
		 'ticket': 2,	
		 'image': 'img/borisov.jpg'},
		   )
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

