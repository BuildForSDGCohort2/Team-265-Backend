from django.shortcuts import render

# Create your views here.
def login_view(request):
    form = LoginModelForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        #obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        #obj.title = form.cleaned_data.get("title")
        obj.user = request.user
        obj.save()
        form = LoginModelForm()
    template_name = "blog/login.html"
    context = {'form': form, 'title': "Sign in to bizKonnect"}
    return render(request, template_name, context)