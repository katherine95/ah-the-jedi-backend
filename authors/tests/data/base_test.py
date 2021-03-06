import os
from django.test import TestCase
from rest_framework.test import APIClient
from PIL import Image
from .data import Data


class BaseTest(TestCase):
    """
    This class 'BaseTest', contains setup used by
    all other tests
    """

    def setUp(self):
        """ Define the test client and required test variables. """

        self.client = APIClient()

        self.base_data = Data()

    def signup_user(self, data=''):
        """
        This method 'signup_user' creates an account
        using the provided details
        """

        data = data or self.base_data.user_data

        return self.client.post(
            "/api/users/",
            data,
            format="json"
        )

    def signup_user2(self, data=''):
        """
        This method 'signup_user' creates an account
        using the provided details
        """

        data = data or self.base_data.user_data2

        return self.client.post(
            "/api/users/",
            data,
            format="json"
        )

    def activate_user(self, uid, token):
        """
        This method 'activate_user' activates a user account
        using the provided details
        """

        return self.client.post(
            "/api/users/activate/?uid={}&token={}".format(uid, token),
            format="json"
        )

    def login_user(self, data=''):
        """
        This method 'login_user'
        attempts to log in a user
        with the data provided
        """

        data = data or self.base_data.login_data

        response = self.client.post(
            "/api/users/login/",
            data,
            format="json"
        )

        return response

    def login_user2(self, data=''):
        """
        This method 'login_user'
        attempts to log in a user
        with the data provided
        """

        data = data or self.base_data.login_data2

        response = self.client.post(
            "/api/users/login/",
            data,
            format="json"
        )

        return response

    def fetch_current_user(self, headers=None):
        """
        This method 'fetch_current_user'
        fetches details of current user
        provided with correct authorization
        """
        if headers:
            return self.client.get(
                "/api/user/",
                format="json",
                HTTP_AUTHORIZATION='Bearer ' + headers
            )

        else:
            return self.client.get(
                "/api/user/",
                format="json"
            )

    def update_user_details(self, data='', token=None):
        """
        This method 'update_user_details'
        updates details of current user with
        the provided data
        """

        data = data or self.base_data.update_data

        if token:
            return self.client.put(
                "/api/user/",
                data,
                format="json",
                HTTP_AUTHORIZATION='Bearer ' + token
            )
        else:
            return self.client.put(
                "/api/user/",
                data,
                format="json"
            )

    def login_user_and_get_token(self, data=""):
        res = self.login_user(data) if data else self.login_user()
        token = res.data['token']

        return token

    def fetch_user_profile(self, username):
        """
        This method 'fetch_user_profile'
        fetches accepts a username and
        fetches a profile with the username
        """

        return self.client.get(
            "/api/profiles/{}".format(username),
            format="json"
        )

    def get_all_profiles(self, token):
        """
        This method accesses the get all
        profiles endpoint which takes a
        token since the route is authenticated
        """

        return self.client.get(
            "/api/profiles/",
            HTTP_AUTHORIZATION='Bearer ' +
            token,
            format="json"
        )

    def generate_image(self):
        """
        This method 'generate_image'
        generates and returns an image
        """

        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'test_files/test.png')
        tempfile = Image.open(file_path)
        image = Image.new('RGB', (100, 100))
        image = image.save('test.png')

        return image

    def update_user_profile(self, username, data='', token='', image=None):
        """
        This method 'update_user_profile'
        updates user profile with the
        details provided.
        """

        data, content_type = data or self.base_data.profile_data, 'json'

        if image is not None:

            content_type = "multipart"

            data.update({"image": image})

        return self.client.put(
            "/api/profiles/{}".format(username),
            data,
            format=content_type,
            HTTP_AUTHORIZATION='Bearer ' + token

        )

    def follow_user(self, username='', token=''):
        """
        This method 'follow_user'
        follows a user given the
        username
        """

        username = username or self.base_data.user_data['username']

        return self.client.post(
            "/api/profiles/{}/follow".format(username),
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def unfollow_user(self, username='', token=''):
        """
        This method 'unfollow_user'
        unfollows a user given the
        username
        """

        username = username or self.base_data.user_data['username']

        return self.client.delete(
            "/api/profiles/{}/unfollow".format(username),
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def fetch_followers(self, token=''):
        """
        This method 'fetch_followers'
        gets the followers of a given
        user provided a username
        """

        return self.client.get(
            "/api/user/followers",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def fetch_following(self, token=''):
        """
        This method 'fetch_following'
        gets the users that the current
        authenticated user follows
        """

        return self.client.get(
            "/api/user/following",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def create_article(self, token=''):
        """
        Method to create an article
        """
        token = token or self.token
        article = self.client.post('/api/articles/',
                                   self.base_data.article_data,
                                   HTTP_AUTHORIZATION='Bearer ' +
                                   token,
                                   format='json')
        return article

    def bookmark_article(self, token='', slug=''):
        """
        Method to bookmark an article
        """
        return self.client.post('/api/articles/{}/bookmark/'.
                                format(slug),
                                self.base_data.article_data,
                                HTTP_AUTHORIZATION='Bearer ' +
                                token,
                                format='json')

    def get_bookmark_article(self, token='', slug=''):
        """
        Method to get a bookmarked article
        """
        return self.client.get('/api/articles/{}/bookmark/'.
                               format(slug),
                               self.base_data.article_data,
                               HTTP_AUTHORIZATION='Bearer ' +
                               token,
                               format='json')

    def delete_bookmark_article(self, token='', slug=''):
        """
        Method to delete a bookmark on an articles
        """
        return self.client.delete('/api/articles/{}/bookmark/'.
                                  format(slug),
                                  HTTP_AUTHORIZATION='Bearer ' +
                                  token,
                                  format='json')

    def fetch_all_notifications(self, token=''):
        """
        This method 'fetch_all_notifications'
        gets all the notification of a specific user
        """

        return self.client.get(
            "/api/notifications/all",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def fetch_read_notifications(self, token=''):
        """
        This method 'fetch_read_notifications'
        gets all the read notifications of a
        given user
        """

        return self.client.get(
            "/api/notifications/read",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def fetch_unread_notifications(self, token=''):
        """
        This method 'fetch_unread_notifications'
        gets all the unread notifications of a
        given user
        """

        return self.client.get(
            "/api/notifications/unread",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def fetch_subscriptions(self, token=''):
        """
        This method 'fetch_subscriptions'
        gets all the subscriptions of a
        given user
        """

        return self.client.get(
            "/api/notifications/subscriptions",
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def update_subscriptions(self, data='', token=''):
        """
        This method 'update_subscriptions'
        handles opt in and out of subscriptions
        """

        data = data or self.base_data.subscription_data

        return self.client.put(
            "/api/notifications/subscriptions",
            data,
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def read_notification(self, id, token):
        """
        This method 'read_notifications'
        marks notifications as read
        """

        return self.client.put(
            "/api/notifications/read/{}".format(id),
            format='json',
            HTTP_AUTHORIZATION='Bearer ' + token
        )

    def create_comment(self, slug):
        """
        This method allows a user to create a Comment
        """
        return self.client.post('/api/articles/{}/comments/'.format(slug),
                                self.base_data.comment_data,
                                HTTP_AUTHORIZATION='Bearer ' +
                                self.token,
                                format='json')

    def delete_comment(self, slug, id, token=''):
        """
        This method allows a user to delete a Comment
        """
        token = token or self.token
        return self.client.delete('/api/articles/{}/comments/?id={}'.format(slug, id),
                                  HTTP_AUTHORIZATION='Bearer ' +
                                  token,
                                  format='json')
