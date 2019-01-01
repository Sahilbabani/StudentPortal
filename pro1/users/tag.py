from django import template

register = template.Library()

@register.assignment_tag
def hello_world(name):
    salute = 'Hello' + name
    return salute

def get_year(email):
    year = email[2]
    return year