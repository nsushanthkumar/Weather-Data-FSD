from django.urls import path
from .import views
# from .views import PostDeleteView
urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<city_name>', views.delete_city, name='delete_city'),
]
