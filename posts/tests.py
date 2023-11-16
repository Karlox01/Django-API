from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='password')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='password')
        response = self.client.post('/posts/', {'title': 'peder'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
        print(len(response.data))

    def test_logged_out_user_can_create_post(self):
        response = self.client.post('/posts/', {'title': 'peder'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
        print(len(response.data))


class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='password')
        brian = User.objects.create_user(username='brian', password='password')
        Post.objects.create(
            owner=adam, title='a title 1', content='my content'
        )
        Post.objects.create(
            owner=brian, title='a title 2', content='my content two' 
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/2/')
        self.assertEqual(response.data['title'], 'a title 2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='password')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
        

    def test_user_can_update_other_posts(self):
        self.client.login(username='brian', password='password')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

        




