from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostModelForm

# Create your views here.

def blog_post_list_view(request):
    template_name = "blog/list.html"
    queryset = BlogPost.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, template_name, context)

# @staff_member_required ---> for staff members
@login_required()
def blog_post_create_view(request):
    template_name = "form.html"
    form = BlogPostModelForm(request.POST or  None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = form.cleaned_data.get("slug").lower()
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    template_name = "blog/detail.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {
        'object' : obj
    }
    return render(request, template_name, context) 

# @staff_member_required ---> for staff members
@login_required()
def blog_post_update_view(request, slug):
    template_name = "form.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or  None, instance=obj)

    if form.is_valid():
        form.save()
        form = BlogPostModelForm() 
    context = {
        'form'   : form,
        'title'  : f"Update { obj.title }"
    }
    return render(request, template_name, context) 

# @staff_member_required ---> for staff members
@login_required()
def blog_post_delete_view(request, slug):
    template_name = "blog/delete.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/blog')

    context = {
        'object' : obj
    }
    return render(request, template_name, context) 