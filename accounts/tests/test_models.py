from mixer.backend.django import mixer
from accounts.models import User, Profile, InstructorResume, InstructorReport
import pytest

@pytest.mark.django_db
class TestModels:
    # def test_user(self):
    #     user = User.objects.create(username='whatever', password='1')
    #     assert user.username == 'whatever'
    def test_instructor_report_rating(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        report = InstructorReport(profile=profile)
        #First rating
        report.add_rating(1)
        assert report.rating == 1
        #Then, mean rating is calculated
        report.add_rating(3)
        assert report.rating == 2

    def test_add_student(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        report = InstructorReport(profile=profile)

        report.add_student()
        assert report.number_of_students == 1

    def test_approve_instructor_resume(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        resume = InstructorResume(profile=profile, degree='D')
        resume.approve()
        assert resume.status == 'accepted'
        assert profile.instructor_application_status == 'accepted'
        assert profile.is_instructor == True

        assert resume.profile.instructor_application_status == 'accepted'
        assert resume.profile.is_instructor == True

    def test_reject_instructor_resume(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        resume = InstructorResume(profile=profile, degree='D')
        resume.reject()
        assert resume.status == 'rejected'
        assert profile.instructor_application_status == 'rejected'
        assert profile.is_instructor == False

        assert resume.profile.instructor_application_status == 'rejected'
        assert resume.profile.is_instructor == False

    def test_submit_instructor_resume(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        resume = InstructorResume(profile=profile, degree='D')
        resume.submit()
        assert resume.status == 'submitted'
        assert profile.instructor_application_status == 'submitted'
        assert profile.is_instructor == False

        assert resume.profile.instructor_application_status == 'submitted'
        assert resume.profile.is_instructor == False

    """
    test_create_profile is a signal test and must be moved to separate test_signals.py file later
    """
    def test_create_profile(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        username = profile.user.username
        assert username == 'whatever'

    def test_show_instructor_application(self):
        user = User.objects.create(username='whatever', password='1')
        profile=user.profile
        # profile=Profile.objects.create(user=user)
        profile.is_instructor = True

        profile.instructor_application_status = 'rejected'
        assert profile.show_instructor_application() == True

        profile.instructor_application_status = 'none'
        assert profile.show_instructor_application() == True

        profile.instructor_application_status = 'submitted'
        assert profile.show_instructor_application() == False
