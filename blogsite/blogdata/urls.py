from django.urls import path
from .views import home, detail, contact, evaluate_contact

app_name  = 'blogdata'

urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:pk>/', detail, name='detail'),
    path('contact-page/', contact, name='contact'),
    path("contact-message-verification/", evaluate_contact, name='ev-contact')
]
