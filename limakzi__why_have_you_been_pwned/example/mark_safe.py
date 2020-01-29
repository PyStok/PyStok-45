# -*- coding: utf-8 -*-
from django.utils import safestring

mystr = "<b>Hello World</b>"
mystr = safestring.mark_safe(mystr)
