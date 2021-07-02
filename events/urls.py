from django.urls import path
  
# importing views from views..py 
from events.views import events, update, create
from . import views
  
urlpatterns = [ 
    path('', views.events, name='events'), 
	path("create/", views.create, name="create"),
	path("update/<int:id>", views.update, name="update"), 
	path("delete/<int:id>", views.delete, name="delete"),
] 
