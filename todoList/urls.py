from django.conf.urls import url
from .views import home,ToDoView,ToDoDetailView


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^api/$', ToDoView.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', ToDoDetailView.as_view()),
    
]
