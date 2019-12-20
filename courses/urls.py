from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='courses'

urlpatterns = [
    url(r'^create_course/$', views.create_course, name='create_course'),
    url(r'^list_courses/$', views.list_courses, name='list_courses'),
    url(r'^edit_course/(?P<oid>[0-9]+)/$', views.edit_course, name='edit_course'),
    url(r'^create_section/(?P<course_id>[0-9]+)/$', views.create_section, name='create_section'),
    url(r'^edit_section/(?P<section_id>[0-9]+)/$', views.edit_section, name='edit_section'),
    url(r'^create_content/(?P<section_id>[0-9]+)/$', views.create_content, name='create_content'),
    url(r'^edit_content/(?P<content_id>[0-9]+)/$', views.edit_content, name='edit_content'),
    url(r'^display_catalog/$', views.display_catalog, name='display_catalog'),
    url(r'^display_catalog/(?P<category_id>[a-zA-Z0-9_ ]*)/$', views.display_catalog, name='display_catalog_category'),
    url(r'^display_catalog/(?P<subcategory>[a-zA-Z0-9_ ]*)/$', views.display_catalog, name='display_catalog_subcategory'),
    url(r'^display_catalog/(?P<type>\w+)/$', views.display_catalog, name='display_catalog_type'),
    url(r'^course_page/(?P<course_id>[0-9]+)/$', views.display_course_page, name='course_page'),
    url(r'^content_play/(?P<content_id>[0-9]+)/$', views.display_content, name='content_play'),

]
