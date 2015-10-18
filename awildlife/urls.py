from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from life import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movement/$', views.movement, name='movement'),
    url(r'^wild-foods/$', views.wild_foods, name='wild_foods'),

    url(r'^faqs/$', TemplateView.as_view(template_name='life/faqs.html'), 
                    name='faqs'),
    
    url(r'^resources/$', TemplateView.as_view(template_name='life/resources.html'), 
                    name='resources'),

    url(r'^about/$', TemplateView.as_view(template_name='life/about.html'), 
                    name='about'),

    url(r'^register/(?P<event_slug>.*)/$', views.register, name='register'),

    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
