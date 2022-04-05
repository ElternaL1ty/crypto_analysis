from django.shortcuts import render

# Create your views here.
def SwaggerView(request):
    return render(request, 'swagger/index.html')