
from django import template

register = template.Library()
# @register.simple_tag(name='img_asset')
@register.filter(name='img_asset')
def img_asset(filename):
    return '/public/storage/img/'+filename
