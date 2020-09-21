from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self, *args, **kwargs):
        print(dir(self))
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title__iexact=title)
        if instance is not None:
            print("Instance is not None")
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            print("qs exist")
            raise forms.ValidationError("This title has already been used. Please use another.")
        return title


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        print(dir(self))
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = Post.objects.filter(title__iexact=title)
        if instance is not None:
            print("Instance is not None")
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            print("qs exist")
            raise forms.ValidationError("This title has already been used. Please use another.")
        return title