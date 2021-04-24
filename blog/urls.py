from django.urls import path
from .views import BlogListView, BlogDetailsView


urlpatterns = [
    path('', BlogListView.as_view(), name ='home'),
    path('post/<int:pk>/', BlogDetailsView.as_view(), name = 'post_detail')
] 