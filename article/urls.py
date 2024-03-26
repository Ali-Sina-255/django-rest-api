from django.urls import path
from . import views


urlpatterns = [
   path('',views.ArticleListCreateApiView.as_view(), name='article_list_view'),
   path('author/',views.JournalistListCreateApiView.as_view(), name='author'),
   path('article-detail/<int:pk>/',views.ArticleDetailApiView.as_view(), name='article-detail'),
]


# urlpatterns = [
#     path('', views.article_list_api_view, name='article'),
#     path('article_detail/<int:value_from_url>/', views.article_detail_api_view, name='article_detail'),
# ]