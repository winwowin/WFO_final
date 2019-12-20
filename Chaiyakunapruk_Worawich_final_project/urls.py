from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [

    path('',
         RedirectView.as_view(
             pattern_name='welcome_urlpattern',
             permanent=False
         )),

    path('login/',
         LoginView.as_view(template_name='companyinfo2/login.html'),
         name='login_urlpattern'
         ),

    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
         ),

    path('about/',
         TemplateView.as_view(
            template_name='companyinfo2/about.html'),
         name='about_urlpattern'
         ),

    path('welcome/',
         TemplateView.as_view(
             template_name='companyinfo2/welcome.html'),
         name='welcome_urlpattern'
         ),

    path('research_product/',
         TemplateView.as_view(
             template_name='companyinfo2/research_product.html'),
         name='research_product_urlpattern'
         ),

    path('news/',
         TemplateView.as_view(
             template_name='companyinfo2/news.html'),
         name='news_urlpattern'
         ),

    path('store/',
         TemplateView.as_view(
             template_name='companyinfo2/store.html'),
         name='store_urlpattern'
         ),

    path('admin/', admin.site.urls),

    path('', include('companyinfo2.urls'))

]