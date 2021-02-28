from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path('', views.index, name="index"),
    path('wiki/<title>', views.entry, name="entry"),
    path('random', views.random_page, name="random"),
    path('search', views.search, name="search"),
    path('create', views.create, name="create"),
    path('edit/<title>', views.edit, name="edit")
]