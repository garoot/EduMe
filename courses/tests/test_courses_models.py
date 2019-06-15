from mixer.backend.django import mixer
from django.test import RequestFactory, TestCase
from courses.models import *
import pytest

@pytest.mark.django_db
class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestModels, cls).setUpClass()
        cls.category = Category.objects.create(name='test_category')
        cls.subcategory = Subcategory.objects.create(subcategory='test_subcategory', category=cls.category)
        cls.course = Course.objects.create(course_name = 'test_course')
        cls.course_section = CourseSection.objects.create(section_name='test_course_section', course=cls.course)
        cls.content_item = ContentItem.objects.create(title='test_content_item', course_section=cls.course_section)
        cls.course_report = CourseReport.objects.create(course=cls.course)
    def test_subcategory(self):
        assert str(self.subcategory) == 'test_subcategory'

    def test_category(self):
        assert str(self.category) == 'test_category'

    def test_course(self):
        assert str(self.course) == 'test_course'

    def test_course_section(self):
        assert str(self.course_section) == 'test_course_section'

    def test_content_item(self):
        assert str(self.content_item) == 'test_content_item'

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
