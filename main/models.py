from django.db import models
from django.utils import timezone

# Create your models here.
class Field(models.Model):
	name_eng = models.CharField(max_length=255)
	name_ar = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name_eng



class Subfield(models.Model):
	name_eng = models.CharField(max_length=255)
	name_ar = models.CharField(max_length=255)
	field = models.ForeignKey('main.Field')
	def __unicode__(self):
		return self.name_eng



class Course(models.Model):
	name_eng = models.CharField(max_length=255)
	name_ar = models.CharField(max_length=255)
	goal_eng = models.TextField()
	goal_ar = models.TextField()
	conditions_eng = models.TextField()
	conditions_ar = models.TextField()
	venue_eng = models.CharField(max_length=255,null=True, blank=True,)
	venue_ar = models.CharField(max_length=255,null=True, blank=True,)
	
	date = models.DateTimeField(null=True, blank=True,)
	price = models.IntegerField(null=True, blank=True,)
	subfield = models.ForeignKey('main.Subfield')
	seats = models.IntegerField()
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	demo = models.BooleanField(default=False)
	icon = models.ImageField(null=True, blank=True, upload_to='course_icons', default='/media/course_icon.jpg')
	big_picture = models.ImageField(null=True, blank=True, upload_to='course_big_picture', default='/media/course_big_picture.png')
	def __unicode__(self):
		return self.name_eng


class Tutor(models.Model):
	name_eng = models.CharField(max_length=255)
	name_ar = models.CharField(max_length=255)
	bio_eng = models.CharField(max_length=255)
	bio_ar = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True, upload_to='tutor image')
	course = models.ForeignKey('main.Course', blank=True , null=True)
	def __unicode__(self):
		return self.name_eng
		
class Registrar(models.Model):
	SEX_CHOICES = (
					('F', 'Female',),
					('M', 'Male',),
					)

	name = models.CharField(max_length=255)
	sex = models.CharField(max_length=1,choices=SEX_CHOICES,)
	date_of_birth = models.DateField()
	degree = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=255)
	email = models.EmailField()
	mailing_list = models.BooleanField()
	address =  models.TextField(null=True, blank=True)
	course = models.ForeignKey('main.Course')
	paid = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class News(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateField()
	icon = models.ImageField(null=True, blank=True, upload_to='course_icons', default='/media/news_icon.jpg')
	body = models.TextField()
	title_ar = models.CharField(max_length=255)
	body_ar = models.TextField()
	def __unicode__(self):
		return self.title

class HomepageHeader(models.Model):
	title_eng = models.CharField(max_length=255)
	title_ar = models.CharField(max_length=255)
	discription_eng = models.CharField(max_length=255)
	discription_ar = models.CharField(max_length=255)
	image_eng = models.ImageField(null=True, blank=True, upload_to='header')
	image_ar =  models.ImageField(null=True, blank=True, upload_to='header')
	url_eng = models.CharField(max_length=255, null=True, blank=True)
	url_ar = models.CharField(max_length=255, null=True, blank=True)

class Image(models.Model):
	title_eng = models.CharField(max_length=255,null=True, blank=True)
	title_ar = models.CharField(max_length=255,null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to='imageGallary')
	def __unicode__(self):
		return self.title_eng






