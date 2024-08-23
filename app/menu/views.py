from django.shortcuts import render


def main_view(request):
    context = {
        'title': 'Main'
    }
    return render(request, 'menu/main.html', context=context)

def about_view(request):
    context = {
        'title': 'About'
    }
    return render(request, 'menu/about.html', context=context)

def contact_view(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'menu/contact.html', context=context)


def contact_view_1(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'menu/contact.html', context=context)
