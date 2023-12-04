from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
        path("",views.music,name="music"),
        path("listen/<int:music_id>/",views.listen,name="listen"),
        path("musiclist/",views.music_url_list,name="url_list"),
        ]
