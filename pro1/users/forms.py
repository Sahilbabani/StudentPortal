# extra email field after inherited form.py
# Registration form

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import branches


class UserRegisterForm(UserCreationForm, forms.ModelForm):
	email = forms.EmailField(required = True)
	first_name = forms.CharField(max_length = 32, required = True)
	last_name = forms.CharField(max_length = 32, required = True)
	branch = forms.ChoiceField(choices=branches)
	
	#default is true that it is required
	# add validation for institute email id

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'branch', 'last_name', 'password1', 'password2']  # in-order

	def clean_email (self) :
		data = self.cleaned_data['email']
		domain = data.split('@')[1]
		if domain != 'btech.nitdgp.ac.in' :
			raise forms.ValidationError('Please make sure that you use college mail address')
		return data
'''
	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.branch=self.cleaned_data['branch']
		if commit:
			user.save()
		return user
'''