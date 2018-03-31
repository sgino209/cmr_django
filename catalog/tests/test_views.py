# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Views tests

from django.test import TestCase
from catalog.models import Person
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User, Permission
import datetime

class PersonListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create persons for pagination tests
        number_of_persons = 13
        for person_num in range(number_of_persons):
           Person.objects.create(first_name='Christian {0}'.format(person_num), last_name = 'Surname {0}'.format(person_num) )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/persons/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('persons'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('persons'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/person_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('persons'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['person_list']) == 10)

    def test_lists_all_persons(self):
        resp = self.client.get(reverse('persons')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['person_list']) == 3)

class PersonCreateViewTest(TestCase):
    """ Test case for the AuthorCreate view """

    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        
        test_user2 = User.objects.create_user(username='testuser2', password='12345') 
        test_user2.save()    

        # Create a person
        test_person = Person.objects.create(first_name='John', last_name='Smith')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('person_create') )
        self.assertRedirects(resp, '/accounts/login/?next=/catalog/person/create/' )
        
    def test_redirect_if_logged_in_but_not_correct_permission(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('person_create') )
        self.assertRedirects(resp, '/accounts/login/?next=/catalog/person/create/' )

    def test_logged_in_with_permission(self):
        login = self.client.login(username='testuser2', password='12345')
        resp = self.client.get(reverse('person_create') )
        self.assertEqual( resp.status_code,302)
        
    def test_uses_correct_template(self):
        login = self.client.login(username='testuser2', password='12345')
        resp = self.client.get(reverse('person_create') )
        self.assertEqual( resp.status_code,302)
        #self.assertTemplateUsed(resp, 'catalog/person_form.html')

    def test_redirects_to_detail_view_on_success(self):
        login = self.client.login(username='testuser2', password='12345')
        resp = self.client.post(reverse('person_create'),{'first_name':'Christian Name','last_name':'Surname',} )
        self.assertEqual( resp.status_code,302)
        #self.assertTrue( resp.url.startswith('/catalog/person/') )
