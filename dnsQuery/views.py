from django.shortcuts import render
from django.http import HttpResponse

from .models import Query

# Create your views here.

def home(request):
    return HttpResponse("Hobby Project<br><br>Author<br>-Valar")

def index(request):

    latest_query_list = Query.objects.order_by('-created')[:5]
    
    context = {
        'latest_query_list': latest_query_list,
    }

    return render(request, 'index.html', context)
