from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)