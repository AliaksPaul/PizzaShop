from django.shortcuts import render


def main(request):
    return render(request, 'pages/main.html')

def page_not_found(request):
    return render(request, '404_template.html')