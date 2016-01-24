# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Journals

def journals_list(request):
	journals = (
		{'id': 1,
		 'last_name': u'Подоба',},
		{'id': 2,
		 'last_name': u'Баланчук',},
		{'id': 3,
		 'last_name': u'Борисов',},
		   )
	return render(request, 'students/journals_list.html', {'journals': journals})

def journals_edit(request, sid):
	return HttpResponse('<h1>Journals Edit %s</h1>' % sid)

