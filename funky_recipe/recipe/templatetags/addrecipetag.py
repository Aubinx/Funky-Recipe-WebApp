from django import template
from recipe.views import *

register = template.Library()


@register.simple_tag
def resultsadd(val=None):
    return globalmessageaddrecipe()