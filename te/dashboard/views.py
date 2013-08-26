from django.shortcuts import render

def home_page(request):
    ctx = {
        'js': 'index.js.html',
        'css': 'index.css.html',
    }
    return render(request, 'index.html', ctx)
