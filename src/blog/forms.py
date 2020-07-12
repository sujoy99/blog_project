from django import forms
from .models import BlogPost

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'image',
            'slug',
            'content',
            'publish_date'
        ]

    def clean_title(self, *agrs, **kwargs):
        instance = self.instance
        print(instance.title)
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if qs is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title is already used")
        return title