from django.shortcuts import render


def main(request):
    return render(request, 'pages/main.html')

def error_404(request, exception):
    return render(request, '404.html')