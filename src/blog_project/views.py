from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import BlogPost


# Create your views here.

def home_view(request):
    template_name = "home.html"
    queryset = BlogPost.objects.all()[:4]
    context = {
        'title': "Welcome to Django",
        'object_list' : queryset
    }
    return render(request, template_name, context)