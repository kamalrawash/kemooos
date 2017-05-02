# -*- coding: utf-8 -*-
from django import forms
from main.models import *



class EmailForm(forms.Form):
	email = forms.EmailField()

class RegisterForm(forms.ModelForm):
		class Meta:
			model = Registrar
			#fields = '__all__'
			exclude = ('course','paid',)


class RegisterFormAR(forms.ModelForm):
		class Meta:
			model = Registrar
			#fields = '__all__'
			exclude = ('course','paid',)
			labels = {
            "name": "الاسم",
            "sex":'الجنس',
            'date_of_birth': 'تاريخ الميلاد',
            'degree': 'المؤهل العلمي',
            'phone_number': 'رقم الهاتف',
            'email': 'الإيميل',
            'mailing_list': '<br>انضم للقائمة البريدية',
            'address':'العنوان',

            
        }