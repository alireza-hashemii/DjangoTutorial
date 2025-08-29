from django.shortcuts import render, redirect
from . models import Blog, UserMessage
from . forms import ContactForm
# Create your views here.

def home(request):
    blogs = Blog.objects.filter(status='p')
    
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    blog = Blog.objects.get(pk=pk)

    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)


def contact(request):
    context = {}
    context['form'] = ContactForm()
    return render(request, 'contact.html', context)

def evaluate_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            new_user_message = UserMessage.objects.create(
                name = name,
                email = email,
                phone_number = phone,
                message = message
            )
            new_user_message.save()
            return redirect('blogdata:home')
        else:
            return redirect('blogdata:contact')
    else:
        return redirect('blogdata:contact')