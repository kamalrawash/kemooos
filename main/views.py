from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from forms import *
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home_eng(request):

	context = {}
	today = datetime.now()
	try:
		context['courses2'] = Course.objects.filter(featured=True, date__gte = today, active = True).order_by('date')[1:3]
	except Exception, e:
		print e
	try:
		context['courses'] = Course.objects.filter(featured=True, date__gte = today, active = True).order_by('date')[:3]
	except Exception, e:
		print e
	try:
		context['news_list1'] = News.objects.order_by('-pk')[:2]
	except Exception, e:
		print e
	try:
		context['news_list2'] = News.objects.order_by('-pk')[2:10]
	except Exception, e:
		print e
	try:
		context['header'] = HomepageHeader.objects.latest('id')
		print 'working'
	except Exception, e:
		print e
	context['form'] = EmailForm()
	print EmailForm()
	if request.method == 'POST':
		form = EmailForm(request.POST)
		
		print '----------------'
		context['form'] = form
		if form.is_valid():
			email = form.cleaned_data.get('email', None)
			data = '{"status": "pending", "email_address": "%s"}' % email
			url = 'https://us14.api.mailchimp.com/3.0/lists/e727deec28/members/'
			r = requests.post(url, data=data ,auth=HTTPBasicAuth('username','bdaae66a75650a127a44fee964a0d6a2-us14'))
			context['emailfilled'] = True
			print r.text
			
	return render(request, 'base.html', context)

def courses(request):
	context = {}
	today = datetime.now()
	context['trainingcourses'] = Course.objects.filter(subfield__field__name_eng = 'training', date__gte = today, active = True)
	context['consultationcourses'] = Course.objects.filter(subfield__field__name_eng = 'consultation', date__gte = today, active = True)
	context['conferancescourses'] = Course.objects.filter(subfield__field__name_eng = 'conferances', date__gte = today, active = True)
	context['bootcampscourses'] = Course.objects.filter(subfield__field__name_eng = 'bootcamps', date__gte = today, active = True)
	print context
	return render(request,'courselist.html', context)

def course(request, pk):
	context = {}
	course = Course.objects.get(pk=pk)
	context['course'] = course
	remaining_seats = course.seats - course.registrar_set.count()
	if remaining_seats <= 0:
		remaining_seats = 0
	context['remaining_seats'] = remaining_seats
	return render(request, 'coursedetails.html', context)

def register(request, pk):
	context = {}
	course = Course.objects.get(pk=pk)
	context['course'] = course
	context['form'] = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		context['form'] = form
		if form.is_valid:
			registrar = form.save(commit=False)
			
			registrar.course = course
			registrar.save()
			context['registrar'] = registrar
			mailing_list =  form.cleaned_data.get('mailing_list', None)
			if mailing_list == True:
				email = form.cleaned_data.get('email', None)
				data = '{"status": "pending", "email_address": "%s"}' % email
				url = 'https://us14.api.mailchimp.com/3.0/lists/3a2b95aa8c/members/'
				r = requests.post(url, data=data ,auth=HTTPBasicAuth('username','bcb9dd5cda03f50703b7358bcb62079d-us14'))
				print r.text
		return render(request, 'confirmed.html', context)

	return render(request, 'register.html', context)

def newsdetails(request, pk):
	context = {}
	news = News.objects.get(pk=pk)
	context['news'] = news
	return render(request, 'newsdetails.html', context)

def galary(request):
	context = {}
	context['image_list'] = Image.objects.all()
	print context
	return render(request, 'imagegalary.html', context)


def newslist(request):
	context = {}
	news_list = News.objects.all().order_by('-pk')

	paginator = Paginator(news_list, 9)

	page = int(request.GET.get("page", '1'))

	try:
		news_list = paginator.page(page)
	except (InvalidPage, EmptyPage):
		news_list = paginator.page(paginator.num_pages)


	context['news_list'] = news_list
	return render(request, 'newslist.html', context)

def aboutus(request):
	context = {}
	return render(request, 'aboutus.html', context)

def ourteam(request):
	context = {}
	return render(request, 'ourteam.html', context)

@staff_member_required
def courselist(request):
	context = {}
	context['courses'] = Course.objects.all()

	return render(request, 'courselistadmin.html', context)


def contactus(request):
	context = {}
	return render(request, 'contactus.html', context)

@staff_member_required
def courseadmin(request, pk):
	context = {}
	context['course'] = Course.objects.get(pk=pk)
	return render(request, 'courseadmin.html', context)



def schedule2018(request):
	context = {}
	try:
		context['loop_times'] = range(1, 15)
	except Exception, e:
		print e

	#context['courses'] = Course.objects.all()
	stdate = datetime(2017, 5, 1)
	enddate = datetime(2018, 12, 30)
	# for descending orde 
	#context['courses'] = Course.objects.filter(featured=True, date__gte=stdate, date__lte=enddate, active = True).order_by('date').reverse()
	#or context['courses'] = Course.objects.filter(featured=True, date__gte=stdate, date__lte=enddate, active = True).order_by('-date')
	context['courses'] = Course.objects.filter(featured=True, date__gte=stdate, date__lte=enddate ).order_by('date')[3:4]
	return render(request, 'schedule2018.html', context)













###############
# arabic site #
###############
def home_ar(request):

	context = {}
	today = datetime.now()
	try:
		context['courses'] = Course.objects.filter(featured=True, date__gte = today, active = True)[:3]
	except Exception, e:
		print e
	try:
		context['news_list1'] = News.objects.order_by('-pk')[:2]
	except Exception, e:
		print e
	try:
		context['news_list2'] = News.objects.order_by('-pk')[2:10]
	except Exception, e:
		print e
	try:
		context['header'] = HomepageHeader.objects.latest('id')
		print 'working'
	except Exception, e:
		print e
	context['form'] = EmailForm()
	print EmailForm()
	if request.method == 'POST':
		form = EmailForm(request.POST)
		
		print '----------------'
		context['form'] = form
		if form.is_valid():
			email = form.cleaned_data.get('email', None)
			data = '{"status": "pending", "email_address": "%s"}' % email
			url = 'https://us14.api.mailchimp.com/3.0/lists/e727deec28/members/'
			r = requests.post(url, data=data ,auth=HTTPBasicAuth('username','bdaae66a75650a127a44fee964a0d6a2-us14'))
			context['emailfilled'] = True
			print r.text
			
	return render(request, 'base_ar.html', context)

def courses_ar(request):
	context = {}
	today = datetime.now()
	context['trainingcourses'] = Course.objects.filter(subfield__field__name_eng = 'training', date__gte = today, active = True)
	context['consultationcourses'] = Course.objects.filter(subfield__field__name_eng = 'consultation', date__gte = today, active = True)
	context['conferancescourses'] = Course.objects.filter(subfield__field__name_eng = 'conferances', date__gte = today, active = True)
	context['bootcampscourses'] = Course.objects.filter(subfield__field__name_eng = 'bootcamps', date__gte = today, active = True)
	print context
	return render(request,'courselist_ar.html', context)

def course_ar(request, pk):
	context = {}
	course = Course.objects.get(pk=pk)
	context['course'] = course
	remaining_seats = course.seats - course.registrar_set.count()
	if remaining_seats <= 0:
		remaining_seats = 0
	context['remaining_seats'] = remaining_seats
	return render(request, 'coursedetails_ar.html', context)

def register_ar(request, pk):
	context = {}
	course = Course.objects.get(pk=pk)
	context['course'] = course
	context['form'] = RegisterFormAR()
	if request.method == 'POST':
		form = RegisterFormAR(request.POST)
		context['form'] = form
		if form.is_valid:
			registrar = form.save(commit=False)
			
			registrar.course = course
			registrar.save()
			context['registrar'] = registrar
			mailing_list =  form.cleaned_data.get('mailing_list', None)
			if mailing_list == True:
				email = form.cleaned_data.get('email', None)
				data = '{"status": "pending", "email_address": "%s"}' % email
				url = 'https://us14.api.mailchimp.com/3.0/lists/3a2b95aa8c/members/'
				r = requests.post(url, data=data ,auth=HTTPBasicAuth('username','bcb9dd5cda03f50703b7358bcb62079d-us14'))
				print r.text
		return render(request, 'confirmed.html', context)

	return render(request, 'register_ar.html', context)

def newsdetails_ar(request, pk):
	context = {}
	news = News.objects.get(pk=pk)
	context['news'] = news
	return render(request, 'newsdetails_ar.html', context)

def galary_ar(request):
	context = {}
	context['image_list'] = Image.objects.all()
	print context
	return render(request, 'imagegalary.html', context)


def newslist_ar(request):
	context = {}
	news_list = News.objects.all().order_by('-pk')

	paginator = Paginator(news_list, 9)

	page = int(request.GET.get("page", '1'))

	try:
		news_list = paginator.page(page)
	except (InvalidPage, EmptyPage):
		news_list = paginator.page(paginator.num_pages)


	context['news_list'] = news_list
	return render(request, 'newslist_ar.html', context)

def aboutus_ar(request):
	context = {}
	return render(request, 'aboutus_ar.html', context)

@staff_member_required
def courselist_ar(request):
	context = {}
	context['courses'] = Course.objects.all()

	return render(request, 'courselistadmin.html', context)


def contactus_ar(request):
	context = {}
	return render(request, 'contactus_ar.html', context)






