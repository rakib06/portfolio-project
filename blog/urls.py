from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.all_blog, name='all_blog'),
    path('<int:blog_id>', blog.views.detail, name='detail'),
    ]