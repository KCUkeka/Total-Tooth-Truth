from django.conf.urls import url
from . import views
                   
urlpatterns = [
    url(r'^$', views.main),
    url(r'^guide_k2$', views.guide_k2),
    url(r'^guide_35$', views.guide_35),
    url(r'^guide_68$', views.guide_68),
    url(r'^guide_high$', views.guide_high),
    url(r'^contact_us$', views.contact_us),
    url(r'^test_k2$', views.test_k2),
    url(r'^test_35$', views.test_35),
    url(r'^test_68$', views.test_68),
    url(r'^test_high$', views.test_high),
    url(r'^brushing$', views.brushing),    
    url(r'^flossing$', views.flossing),     
    url(r'^field_trip$', views.field_trip),   
    url(r'^fun_color$', views.fun_color),    
    url(r'^fun_video$', views.fun_video),    
    url(r'^fun_games$', views.fun_games),    
    url(r'^fun_experiments$', views.fun_experiments),    
]