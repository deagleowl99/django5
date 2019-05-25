from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.archive, name='archive'),
    path('article/<article_id>/', views.get_article, name='get_article'),
	path('new', views.create_post, name = 'create_post'),
]
