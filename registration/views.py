from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("login") + '?registration'
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificaré las clases en tiempo de ejecución. Podría haberlo hecho en el template directamente(como he hecho con el login, pero en este
        #caso no me interesa ya que perdería las validaciones que vienen con este formulario(longitud, caracteres especiales...)
        form.fields["username"].widget = forms.TextInput(attrs={"class": "border-2 border-black rounded-sm w-full mb-2 mt-2 p-2", "placeholder": "Username"})
        form.fields["email"].widget = forms.EmailInput(attrs={"class": "border-2 border-black rounded-sm w-full mb-2 mt-2 p-2", "placeholder": "Email"})
        form.fields["password1"].widget = forms.PasswordInput(attrs={"class": "border-2 border-black rounded-sm w-full mb-2 mt-2 p-2", "placeholder": "Password"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={"class": "border-2 border-black rounded-sm w-full mb-2 mt-2 p-2", "placeholder": "Repeat your password"})
        return form