from django.shortcuts import render,redirect
import datetime
from django.views.decorators.csrf import csrf_protect
from models import *
from django.http import *
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
@csrf_protect
def home(request):
	today=str(datetime.date.today())
	if Diary.objects.filter(date=today).exists():
		diary=Diary.objects.get(date=today)
		article=diary.article
	else:
		article=''
	diarys=[]
	today=datetime.date.today()

	for i in xrange(13):
		date=today-datetime.timedelta(days=i+1)
		if Diary.objects.filter(date=date).exists():
			diary=Diary.objects.get(date=date).article
		else:
			diary=''	
		diarys.append(diary)
	diarys.reverse()
	return render(request,'diary/index.html',{'article':article,'diarys':diarys})

def saveArticle(request):
	print "saveArticle"
	today=str(datetime.date.today())
	if Diary.objects.filter(date=today).exists():
		diary=Diary.objects.get(date=today)
	else:
		diary=Diary(date=today)
	# print request.POST['article']
	diary.article=request.POST['article']
	# print diary.article
	diary.save()
	return HttpResponse("")

