# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
 
# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})
 
# Create a JSON POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format='json')
 
# Explicitly encode
request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json')
 
# Force CSRF validation
factory = APIRequestFactory(enforce_csrf_checks=True)
 
# Client calls
client = APIClient()
client.post('/notes/', {'title': 'new idea'}, format='json')
 
# Inspecting data not rendered content (not an issue since client separate)
response = self.client.get('/users/4/')
self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})
 
# Example
class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
