from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from puzzel_app.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent
def index(request, *args, **kwargs):
    return index2(request, *args, **kwargs)


def index2(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    try:
        percent = (qs.count() * 100.0/ queryset.count())
    except:
        percent = 0    
    qs = PageVisit.objects.filter(path=request.path)
    my_context = {
        "page_title" : "home page",
        "queryset" : queryset.count(),
        "percent" : percent,
        "total_visit_counts" : qs.count() 
    }

    PageVisit.objects.create(path=request.path)
    html_inheritance = "inheritance.html"
    return render(request, html_inheritance, my_context)
