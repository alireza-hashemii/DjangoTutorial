from django.urls import path
from .views import home, detail

app_name  = 'blogdata'

urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:pk>/', detail, name='detail')
]
