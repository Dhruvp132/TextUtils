from . import views
from django.urls import path

urlpatterns = [
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name = 'analyze'),
    
]
