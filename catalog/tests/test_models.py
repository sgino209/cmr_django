# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Models tests

from django.test import TestCase
from catalog.models import Person

class PersonModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Person.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'שם פרטי')
        
    def test_last_name_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'שם משפחה')

    def test_date_of_birth_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label,'תאריך לידה')

    def test_age_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('age').verbose_name
        self.assertEquals(field_label,'גיל')

    def test_first_name_max_length(self):
        person=Person.objects.get(id=1)
        max_length = person._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_last_name_max_length(self):
        person=Person.objects.get(id=1)
        max_length = person._meta.get_field('last_name').max_length
        self.assertEquals(max_length,100)
        
    #def test_object_name_is_last_name_comma_first_name(self):
    #    person=Person.objects.get(id=1)
    #    expected_object_name = '{0}, {1}'.format(person.last_name,person.first_name)
    #    self.assertEquals(expected_object_name,str(person))

