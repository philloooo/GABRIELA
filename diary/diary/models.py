from django.db import models
from django.contrib.auth.models import User
import datetime

class Diary(models.Model):
	article=models.CharField(max_length=750,default="")
	date=models.CharField(max_length=20,unique=True)
