from mixer.backend.django import mixer
from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.storage.fallback import FallbackStorage
from courses.views import *
from courses.models import *
from courses.forms import *
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
import pytest
import unittest


@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.user = mixer.blend(User)
        cls.factory = RequestFactory()
        cls.course = Course.objects.create(course_name = 'test_views_course')
        cls.course_section = CourseSection.objects.create(section_name='test_views_course_section', course=cls.course)
        cls.content_item = ContentItem.objects.create(title='test_views_content_item', course_section=cls.course_section)
        cls.course_report = CourseReport.objects.create(course=cls.course)
        cls.category = Category.objects.create(name='test_views_category')
        cls.subcategory = Subcategory.objects.create(subcategory='test_views_subcategory', category=cls.category)
        cls.section_form = CourseSectionForm(data={'section_num':'2', 'section_name':'test_views_section_form'})

        # file_mock = mock.MagicMock(spec=File, name='FileMock')
        upload_image = open('./media/courses/test/testing.jpg', 'rb')
        # image = {'course_picture': SimpleUploadedFile(upload_image.name(), upload_image.read())}
        image = {'course_picture': SimpleUploadedFile(name='testing.jpg', content=upload_image.read(), content_type='image/jpg')}
        category_id = cls.category.id
        subcategory_id = cls.subcategory.id
        cls.course_form = CourseInfoForm(data={
                            'course_name':'test_views_course_name',
                            'course_topic': 'test_view_course_topic',
                            'course_price': 200.00,
                            'course_title': 'test_views_course_title',
                            'course_outline': 'test_views_course_outline',
                            'course_requirements': 'test_views_course_requirements',
                            'course_outcomes': 'test_views_course_outcomes',
                            'course_description': 'test_views_course_description',
                            'target_students': 'test_views_target_students',
                            'course_category': Category.objects.get(pk=category_id).pk,
                            'course_subcategory': Subcategory.objects.get(pk=subcategory_id).pk
                            }, files=image)
    @classmethod
    def tearDownClass(cls):
        # cls.subcategory.destroy()
        # cls.course.destroy()
        # cls.course_section.destroy()
        # cls.content_item.destroy()
        # cls.course_report.destroy()
        # cls.category.destroy()
        del cls.category
        del cls.subcategory
        del cls.course
        del cls.course_report
        del cls.course_section
        del cls.content_item
        del cls.section_form

    # def test_index(self):
    #     path = reverse('courses:')
    def test_display_course_page(self):
        path = reverse('courses:course_page', args=[self.course.id])
        request = self.factory.get(path)

        response = display_course_page(request, self.course.id)
        assert response.status_code == 200

    def test_display_catalog(self):
        path = reverse('courses:display_catalog')
        request = self.factory.get(path)
        response = display_catalog(request)
        assert response.status_code == 200

        path = reverse('courses:display_catalog_category', args=[self.category])
        request = self.factory.get(path)
        response = display_catalog(request, category_id=self.category.id)
        assert response.status_code == 200

    def test_create_content(self):
        path = reverse('courses:create_content', args=[self.course_section.id])
        request = self.factory.get(path)
        request.user = self.user
        response = create_content(request, section_id=self.course_section.id)
        assert response.status_code == 200

    def test_edit_content(self):
        path = reverse('courses:create_content', args=[self.content_item.id])
        request = self.factory.get(path)
        request.user = self.user
        response = edit_content(request, content_id=self.content_item.id)
        assert response.status_code == 200

    def test_create_section(self):
        path = reverse('courses:create_section', args=[self.course.id])
        request = self.factory.get(path)
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        request.method = 'POST'
        response = create_section(request, course_id=self.course.id, section_form=self.section_form)
        assert response.status_code == 302

        request.method = 'GET'
        response = create_section(request, course_id=self.course.id)
        assert response.status_code == 200

    def test_edit_section(self):
        path = reverse('courses:edit_section', args=[self.course_section.id])
        request = self.factory.get(path)
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        request.method = 'POST'
        response = edit_section(request, section_id=self.course_section.id, edit_section_form=self.section_form, test_save=True)
        assert response.status_code == 302

        request.method = 'GET'
        response = edit_section(request, section_id=self.course_section.id)
        assert response.status_code == 200

        request.method = 'POST'
        response = edit_section(request, section_id=self.course_section.id, edit_section_form=self.section_form, test_delete=True)
        assert response.status_code == 302

    def test_create_course(self):
        path = reverse('courses:create_course')
        request = self.factory.get(path)
        request.user = self.user

        request.method = 'GET'
        response = create_course(request)
        assert response.status_code == 200

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        request.method = 'POST'
        response = create_course(request, new_course_form=self.course_form)
        assert response.status_code == 302
