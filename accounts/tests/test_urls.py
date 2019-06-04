from django.urls import resolve, reverse

class TestUrls:

    def test_login(self):
        path = reverse('accounts:login')
        assert resolve(path).view_name == 'accounts:login'

    def test_register(self):
        path = reverse('accounts:register')
        assert resolve(path).view_name == 'accounts:register'

    def test_instructor_application(self):
        path = reverse('accounts:instructor_application')
        assert resolve(path).view_name == 'accounts:instructor_application'

    def test_dashboard(self):
        path = reverse('accounts:dashboard')
        assert resolve(path).view_name == 'accounts:dashboard'

    def test_edit_profile(self):
        path = reverse('accounts:edit_profile')
        assert resolve(path).view_name == 'accounts:edit_profile'

    def test_list_applications(self):
        path = reverse('accounts:list_applications')
        assert resolve(path).view_name == 'accounts:list_applications'

    def test_display_application(self):
        path = reverse('accounts:display_application', args = [1])
        assert resolve(path).view_name == 'accounts:display_application'

    def test_process_application(self):
        path = reverse('accounts:process_application', args = [1, 1])
        assert resolve(path).view_name == 'accounts:process_application'
