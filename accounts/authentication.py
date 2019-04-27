from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class EmailAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("username:{}".format(username))

        """
        retrieving the username entered by user, and check if it's an email
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
