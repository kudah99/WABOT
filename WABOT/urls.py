from django.contrib import admin
from django.urls import path, include, re_path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

admin.site.site_header  =  "Ballot Buddies Admin Panel"  
admin.site.site_title  =  "Ballot Buddies Admin Panel"
admin.site.index_title  =  "Ballot Buddies  APP"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('whatsapp/', include('hook.urls')),
    path(r'', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    path(r'', include('home.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)