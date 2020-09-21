from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#from django.utils import timezone
# Create your views here.
from .models import Post


def post_list_view(request):
    #list out objects
    #now = timezone.now()
    qs = Post.objects.all()
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    #qs = Post.objects.filter(publish_date__lte=now)
    #qs = Post.objects.filter(title__icontains='My') #queryset -> list of python object
    template_name = "blog/list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)

#@login_required
@staff_member_required
def post_create_view(request):
    #create objects
    # if not request.user.is_authenticated:
    #     return render(request, "not-a-user.html", {})
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        #obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        #obj.title = form.cleaned_data.get("title")
        obj.user = request.user
        obj.save()
        form = PostModelForm()
    template_name = "form.html"
    context = {'form': form, 'title': "Create New Project on CrowdKonnect"}
    return render(request, template_name, context)

def post_detail_view(request, slug):
    #     queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404

    # obj =queryset.last() 
    obj = get_object_or_404(Post, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def post_update_view(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def post_delete_view(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/post")
    if request.method == "POST2":
        return redirect("/post")
    context = {"object": obj}
    return render(request, template_name, context)



    # CRUD -> Create | Retrie
    # GET -> Retrieve, List
    # POST -> Create, Update, Delete