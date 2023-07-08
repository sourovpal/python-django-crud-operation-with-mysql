
from django import template

register = template.Library()

"""'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'libraries':{
            'post_tags': 'app.templatetags.post_tags', <=============== This libraries
            
        }
    },
"""

"""

html page

{% load post_tags %}


"""

@register.filter(name='img_asset')
def img_asset(filename, x):
    return 'public/storage/img/'+filename


#use
#{{value|img_asset:"x"}}



@register.simple_tag(name='img_asset')
def img_asset(filename, x):
    return 'public/storage/img/'+filename

#use
#{% img_asset "filename" "x" %}




@register.inclusion_tag('users.html')
def show_name():
      obj = {'name':'google'}
      return {'obj': obj}
  
#use
#{% show_users %}


@register.tag
def sum(a, b):
      return a + b
  
#use
#{% sum 10 15 %}