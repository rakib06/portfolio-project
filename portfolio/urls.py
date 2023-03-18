
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import blog.views
import blog.views
import visitor.views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    # path('jobgf/', include('jobs.urls')),
    path('', jobs.views.home, name='home'),
    path('bbb', blog.views.all_blog, name='blog_home'),
    path('v/', visitor.views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

