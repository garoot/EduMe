from mixer.backend.django import mixer
from django.test import RequestFactory, TestCase
from courses.models import *
import pytest

@pytest.mark.django_db
class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.category = Category.objects.create(name='test_models_category')
        cls.subcategory = Subcategory.objects.create(subcategory='test_models_subcategory', category=cls.category)
        cls.course = Course.objects.create(course_name = 'test_models_course')
        cls.course_section = CourseSection.objects.create(section_name='test_models_course_section', course=cls.course)
        cls.content_item = ContentItem.objects.create(title='test_models_content_item', course_section=cls.course_section)
        cls.course_report = CourseReport.objects.create(course=cls.course)

    @classmethod
    def tearDownClass(cls):
        # cls.subcategory.destroy()
        # cls.course.destroy()
        # cls.course_section.setroy()
        # cls.content_item.destroy()
        # cls.course_report.destroy()
        # cls.category.destroy()
        del cls.category
        del cls.subcategory
        del cls.course
        del cls.course_report
        del cls.course_section
        del cls.content_item
        
    def test_subcategory(self):
        assert str(self.subcategory) == 'test_models_subcategory'

    def test_category(self):
        assert str(self.category) == 'test_models_category'

    def test_course(self):
        assert str(self.course) == 'test_models_course'

    def test_course_section(self):
        assert str(self.course_section) == 'test_models_course_section'

    def test_content_item(self):
        assert str(self.content_item) == 'test_models_content_item'

    def test_course_report_rating(self):
        course_report = self.course_report

        course_report.add_rating(1)
        assert course_report.rating == 1

        course_report.add_rating(3)
        assert course_report.rating == 2

        course_report.num_buyers = 0

    def test_course_report_update_num_buyers(self):
        course_report = self.course_report

        course_report.update_num_buyers()
        assert course_report.num_buyers == 1

    def test_course_report_update_num_visitors(self):
        course_report = self.course_report

        course_report.update_num_visitors()
        assert course_report.num_visitors == 1
