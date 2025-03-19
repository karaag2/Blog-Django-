from unicodedata import category
from django import forms
from blog.models import BlogPost

JOBS = (
    ("Pyhton", "Developpeur Python"),
    ("JavaScript", "Developpeur JavaScript"),
    ("Rust", "Developpeur Rust"),
)

class SignUpForm(forms.Form):
    pseudo = forms.CharField(label="votre pseudo",max_length=24, required=True)
    email = forms.EmailField()
    password = forms.CharField( min_length=6, required=False,widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
    
class CreateArticle(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "category",
            "date",
            "description",
        ]