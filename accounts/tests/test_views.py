from mixer.backend.django import mixer
from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.storage.fallback import FallbackStorage
from accounts.views import *
from accounts.models import User, Profile, InstructorResume
from accounts.forms import  InstructorResumeForm

import pytest

@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.user = mixer.blend(User)
        profile = mixer.blend(Profile, user=cls.user, instructor_application_status='None')
        cls.profile = profile
        cls.resume = mixer.blend(InstructorResume, profile=cls.user.profile, status='None')
        cls.application_form = InstructorResumeForm(data={'degree':'D', 'major':'Biology', 'experience':'Bachelor\'s degree'})

    def test_user_login(self):
        path = reverse('accounts:login')
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user

        response = user_login(request)
        assert response.status_code == 200

    # def test_user_logout(self):
    #     path = reverse('accounts:logout')
    #     request = RequestFactory().get(path)
    #     request.user = mixer.blend(User)
    #
    #     login(request, request.user)
    #     response = user_logout(request)
    #     assert response.status_code == 200

    def test_register(self):
        path = reverse('accounts:register')
        request = self.factory.get(path) #cls.factory
        request.method = 'GET'
        request.user = self.user #cls.user

        response = register(request)
        assert response.status_code == 200

        """
        pass UserRegistrationForm and test POST
        """

    def test_dashboard(self):
        path = reverse('accounts:dashboard')
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user

        response = dashboard(request)
        assert response.status_code == 200

    def test_edit_profile(self):
        path = reverse('accounts:edit_profile')
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user

        request.method = 'GET'
        response = edit_profile(request)
        assert response.status_code == 200

        request.method = 'POST'
        response = edit_profile(request)
        assert response.status_code == 200
    """
    Given:
    1. id of populated application
    2. populated application_form
    Description:
    1. if passed the two object above, use them to test application.submit()
    2. if not passed, create one based on user's entries in function (outside of test scope)
    Expected output:
    1. application.status == 'submitted'
    2. profile.instructor_application_status == 'submitted'
    """
    def test_instructor_application(self):
        application = self.resume
        oid = application.id
        application_form = self.application_form

        path = reverse('accounts:instructor_application')
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user
        # request.user.profile = None
        """
        1. create a setup def and populate objects: user and profile
        2. then test here
        """
        request.method = 'GET'
        response = instructor_application(request, application_form, oid)
        assert response.status_code == 200

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        """
        POST with invalid form
        Test the form in test_forms.py
        """
        request.method = 'POST'
        response = instructor_application(request, application_form, oid)
        application.refresh_from_db()
        request.user.refresh_from_db()
        assert application.status == 'submitted'
        assert request.user.profile.instructor_application_status == 'submitted'
        assert response.status_code == 200

    def test_approve_application(self):
        application = self.resume
        print("resume id: {}".format(application.id))
        approved = '1'
        oid = application.id
        path = reverse('accounts:process_application', args=(approved, oid,))
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user
        request.method = 'POST'
        response = process_application(request, approved=approved, oid=oid)
        # application.approve()
        application.refresh_from_db()
        request.user.refresh_from_db()
        assert application.status == 'accepted'
        assert request.user.profile.instructor_application_status == 'accepted'
        # assert self.user.profile.is_instructor == True
        assert response.status_code == 200

    def test_reject_application(self):
        application = self.resume
        print("resume id: {}".format(application.id))
        approved = '0'
        oid = application.id
        path = reverse('accounts:process_application', args=(approved, oid,))
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user
        request.method = 'POST'
        response = process_application(request, approved=approved, oid=oid)
        # application.approve()
        application.refresh_from_db()
        request.user.refresh_from_db()
        assert application.status == 'rejected'
        assert request.user.profile.instructor_application_status == 'rejected'
        # assert self.user.profile.is_instructor == True
        assert response.status_code == 200

    def test_display_application(self):
        application = self.resume
        oid = application.id
        path = reverse('accounts:display_application', args=(oid,))
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user
        response = display_application(request, oid=oid)
        assert response.status_code == 200

    def test_list_applications(self):
        path = reverse('accounts:list_applications')
        request = self.factory.get(path) #cls.factory
        request.user = self.user #cls.user
        response = list_applications(request)
        assert response.status_code == 200
