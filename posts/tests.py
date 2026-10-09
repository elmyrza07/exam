from django.test import SimpleTestCase
from django.urls import resolve, reverse

from posts.forms import PostForm
from posts.views import create_post, post_detail, post_list, toggle_complete


class PostAppTests(SimpleTestCase):
    def test_post_list_url_works(self):
        self.assertEqual(resolve('/').func, post_list)

    def test_post_detail_url_works(self):
        self.assertEqual(resolve('/post/1/').func, post_detail)

    def test_create_post_url_works(self):
        self.assertEqual(resolve('/post/create/').func, create_post)

    def test_toggle_complete_url_works(self):
        self.assertEqual(resolve('/post/1/toggle/').func, toggle_complete)

    def test_post_form_has_required_fields(self):
        form = PostForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('is_completed', form.fields)

    def test_post_urls_names(self):
        self.assertEqual(reverse('post_list'), '/')
        self.assertEqual(reverse('post_detail', args=[1]), '/post/1/')
        self.assertEqual(reverse('create_post'), '/post/create/')
        self.assertEqual(reverse('toggle_complete', args=[1]), '/post/1/toggle/')
