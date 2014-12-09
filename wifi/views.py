from django.http import HttpResponse
import os
from django.conf import settings

def home(request):
	x='<ul>'
	for root, dirs, files in os.walk(settings.MEDIA_ROOT):
		#print root,root.strip(settings.MEDIA_ROOT)
		#st='/media/'+root.strip(settings.MEDIA_ROOT)
		for cf in files:
			x+='<li><a href="{0}/{1}">{1}</a></li>'.format(root.replace(settings.MEDIA_ROOT,'/media/'),cf)
	x+='</ul>'
	return HttpResponse(x)
