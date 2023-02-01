from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name = 'news_home'),
    path('add_news', views.add_news, name='add_news'),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewDeleteView.as_view(), name='news-delete')
]