from django.urls import  path
from django.conf.urls.static import static
from django.conf import settings
from .views import add_movie, delete_me, home_view,get_movie, update
app_name='module1'
urlpatterns=[
    path('',home_view,name='home'),
    path('movie/<int:movie_id>/',get_movie,name='search'),
    path('register',add_movie,name='add_movie'),
    path('edit/<int:id>/',update,name='edit'),
    path('delete/<int:id>/',delete_me,name='delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
