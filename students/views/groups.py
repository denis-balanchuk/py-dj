# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#Views for Groups

def groups_list(request):
	groups = (
		{'id': 1,
		 'name_of_group': u'МтМ-21',
		 'starosta': u'Ячмінов Олег',
		 },
		{'id': 2,
		 'name_of_group': u'МтМ-22',
		 'starosta': u'Віталій Подоба',
		 },
		{'id': 3,
		 'name_of_group': u'МтМ-23',
		 'starosta': u'Назаров Андрій',
		 },
		)
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)

