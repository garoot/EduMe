"""coursatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from courses import views
# from search import views as search_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^$', views.index, name='index'),
    # path('Registration/', include('Authentication.urls')),
    # # path('studentsPage/', include('Authentication.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    # url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^search/', search_views.search, name='search_course'),
    # url(r'^search_course/', search_views.search_course, name='search_course'),
    url(r'^$', views.index, name='index'),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # url(r'^payment/', include('payment.urls', namespace='payment')),
]

"""
this is only temporary for development and will be changed in production
"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# ... the rest of your URLconf goes here ...

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
