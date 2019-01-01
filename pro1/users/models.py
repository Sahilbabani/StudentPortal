from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

branches = (
        ('cs', 'Computer Science and Engineering'), 
        ('ec', 'Electronics and Communication Engineering'),
        ('ee', 'Electrical Engineering'),
        ('mm', 'Metallurgical and Materials Engineering'),
        ('bt', 'Biotechnology'),
        ('it', 'Information Technology'),
        ('cv', 'Civil Engineering'),
        ('cm', 'Chemical Engineering'),)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    branch = models.CharField(max_length=25,choices=branches, default='None')
    
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
'''
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    key = models.CharField(max_length=35, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user
'''
post_save.connect(create_user_profile, sender=User)
