from django.shortcuts import render

from te.settings.base import TEMPLATE_THEME

def home_page(request):
    return render(request, TEMPLATE_THEME+'/index.html')
