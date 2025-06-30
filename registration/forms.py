from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required= True, help_text="Required. 254 character max")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "description", "link"]
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "bg-slate-800 rounded-sm p-1 border-2 border-black w-full mb-2"}),
            "description": forms.Textarea(attrs={"class": "bg-slate-800 rounded-sm p-1 border-2 border-black w-full mb-2", "placeholder":"Description"}),
            "link": forms.URLInput(attrs={"class": "bg-slate-800 rounded-sm p-1 border-2 border-black w-full mb-2", "placheholder" : "Link"})
        }

class EmailChangeForm(forms.ModelForm):
    email = forms.EmailField(required= True, help_text="Required. 254 character max")
    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "email" in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email already exists")
        return email