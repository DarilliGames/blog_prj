from django.shortcuts import render

# Create your views here.
def get_main(request):
    return render(request, "blog/index.html")