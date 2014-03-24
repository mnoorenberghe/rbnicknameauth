from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from reviewboard.accounts.backends import AuthBackend, StandardAuthBackend
from reviewboard.extensions.base import Extension, JSExtension
from reviewboard.extensions.hooks import AuthBackendHook


class NicknameAuthBackend(StandardAuthBackend):
    backend_id = 'nickname_auth'
    name = _('Nickname Authentication')

    login_instructions = _("Enter a nickname. No registration required.")
    settings_form = None
    supports_change_email = False
    supports_change_name = False
    supports_change_password = False
    # We auto-create during login so we don't need a registration form
    supports_registration = False

    def authenticate(self, username, password):
        user =  StandardAuthBackend.authenticate(self, username, password)

        if user:
            return user

        UserModel = get_user_model()
        user, created = UserModel.objects.get_or_create(**{
            UserModel.USERNAME_FIELD: username
        })

        # Don't give access to staff or superuser accounts
        if user.is_staff or user.is_superuser:
            return None

        if created:
            user = self.configure_user(user)

        return user

    def get_or_create_user(self, username, request):
        print request
        return StandardAuthBackend.get_or_create_user(self, username, request)

    def configure_user(self, user):
        print dir(user)
        self.update_password(user, "mysupersecurepassword")
        return user

class NicknameAuthJSExtension(JSExtension):
    model_class = 'RBNicknameAuth.Extension'


class RBNicknameAuthExtension(Extension):
    """
    """
    metadata = {
        'Name': 'Nickname Authentication',
    }

    js_extensions = [NicknameAuthJSExtension]

    css_bundles = {
        'default': {
            'source_filenames': ['css/nickname_auth.less'],
        }
    }

    js_bundles = {
        'default': {
            'source_filenames': ['js/nickname_auth.js'],
        }
    }

    def initialize(self):
        AuthBackendHook(self, NicknameAuthBackend)
