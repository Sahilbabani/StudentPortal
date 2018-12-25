# extra email field after inherited form.py
# Registration form

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required = True)
	first_name = forms.CharField(max_length = 32, required = True)
	last_name = forms.CharField(max_length = 32, required = True)
	branch = forms.ChoiceField(choices=[
		(1, 'Computer Science and Engineering'), 
		(2, 'Electronics and Communication Engineering'),
		(3, 'Electrical Engineering'),
		(4, 'Metallurgical and Materials Engineering'),
		(5, 'Biotechnology'),
		(6, 'Information Technology'),
		(7, 'Civil Engineering'),
		(8, 'Chemical Engineering'),
		])

	#default is true that it is required
	# add validation for institute email id

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'branch', 'password1', 'password2']  # in-order

	def clean_email (self) :
		data = self.cleaned_data['email']
		domain = data.split('@')[1]
		if domain != 'btech.nitdgp.ac.in' :
			raise forms.ValidationError('Please make sure that you use college mail address')
		return data
