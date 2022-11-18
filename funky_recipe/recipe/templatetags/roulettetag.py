from django import template
from recipe.views import *

register = template.Library()


@register.simple_tag
def resultsroulette(val=None):
    return globalmessage()
