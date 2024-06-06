
from django.test import TestCase
from django.urls import reverse , resolve
from .views import index, resume, projects, contact

class IndexViewTest(TestCase):

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        
class ContactViewTest(TestCase):

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact.html')
        
        
class URLTests(TestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_resume_url(self):
        url = reverse('resume')
        self.assertEqual(resolve(url).func, resume)

    def test_projects_url(self):
        url = reverse('projects')
        self.assertEqual(resolve(url).func, projects)

    def test_contact_url(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)        