from django.http import HttpResponse
import os
from django.conf import settings

def home(request):
	x="<ul>"
	for root, dirs, files in os.walk(settings.MEDIA_ROOT):
		#print root,root.strip(settings.MEDIA_ROOT)
		#st='/media/'+root.strip(settings.MEDIA_ROOT)
		for cf in files:
			x+='<li><a href="{0}/{1}">{1}</a></li>'.format(root.replace(settings.MEDIA_ROOT,'/f/'),cf)
	x+='</ul>'
	return HttpResponse(x)

def fp(request,p):
	print p
	x="""
<link href="http://vjs.zencdn.net/4.9/video-js.css" rel="stylesheet">
<script src="http://vjs.zencdn.net/4.9/video.js"></script>
<div style="border:1px solid #ccc">  
  <video id="example_video_1" class="video-js vjs-default-skin" controls preload="auto" width="640" height="264" data-setup='{"example_option":true}'>    
	    <source src='/media/"""+p+"""' type='video/mp4' />
	    <!--supported types = video/mp4,video/webm,video/ogg-->
	    <p class="vjs-no-js">To view this video please enable JavaScript</p>
	</video>
</div>
	"""
	return HttpResponse(x)
