from django.test import TestCase
from django.contrib.auth import get_user_model


def create_user_helper_function(**payload):
    return get_user_model().objects.create_user(**payload)


class TestModel(TestCase):
    """ test user model """

    def setUp(self) -> None:
        self.payload = {'password': 'TestPass123!',
                        'email': 'jan@test60.pl',
                        }

    def test_user_creation(self) -> None:
        user = create_user_helper_function(**self.payload)

        self.assertEqual(user.email, self.payload['email'])
        self.assertTrue(user.check_password(self.payload['password']))

    # def test_check_signal(self) -> None:
    #     """ test if profile is created """

    #     user = get_user_model().objects.create_user(**self.payload)
    #     profile = User.objects.get(user=user)

    #     self.assertEqual(str(profile), self.payload['email'])

    def test_check_email_normalize(self) -> None:
        payload = {
            'email': 'TEST@TesT.pl',
            'password': 'test'
        }

        user = user = create_user_helper_function(**payload)

        self.assertEqual(user.email, 'TEST@test.pl')

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """ Test superuser is created """

        user = get_user_model().objects.create_superuser(
            'test@test.pl',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
