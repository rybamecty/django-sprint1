from django.shortcuts import render


def about(request):
    """View-функция для страницы 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """View-функция для страницы 'Наши правила'."""
    return render(request, 'pages/rules.html')
