from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.all_blog, name='home'),

    ]