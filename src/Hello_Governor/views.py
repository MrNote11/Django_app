from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from puzzel_app.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent
def index(request, *args, **kwargs):
    my_context = {
        "page_title" : "home page",
    }
    html_title = "home.html"
    return render(request, html_title, my_context)


def index2(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    qs = PageVisit.objects.filter(path=request.path)
    my_context = {
        "page_title" : "home page",
        "queryset" : queryset.count(),
        "percent" : (qs.count() * 100.0/ queryset.count()),
        "total_visit_counts" : qs.count() 
    }

    PageVisit.objects.create(path=request.path)
    html_inheritance = "inheritance.html"
    return render(request, html_inheritance, my_context)
