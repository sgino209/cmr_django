# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Models creation

from django.db import models
from django.urls import reverse #Used to generate urls by reversing the URL patterns

class Person(models.Model):
    """ Model representing a person """

    GENDER = (
        ('m', 'זכר'),
        ('f', 'נקבה'),
    )

    id_num = models.CharField('תעודת זהות', max_length=10, help_text='כולל ספרת ביקורת')
    first_name = models.CharField('שם פרטי', max_length=100)
    last_name = models.CharField('שם משפחה', max_length=100)
    gender= models.CharField('מין', max_length=1, choices=GENDER, blank=True, default='d', help_text='זכר/נקבה')
    date_of_birth = models.DateField('תאריך לידה', null=True, blank=True, help_text='yyyy-mm-dd')
    age = models.CharField('גיל', max_length=3, help_text='[שנים]')
    address = models.CharField('כתובת', max_length=100, help_text='רחוב, מספר בית, כניסה')
    city = models.CharField('עיר', max_length=20, help_text='לדוגמא: ק.מוצקין')
    phone1 = models.CharField('טלפון1', max_length=100, help_text='טלפון ראשי, כולל קידומת')
    phone2 = models.CharField('טלפון2', max_length=100, help_text='טלפון משני, כולל קידומת')
    phone3 = models.CharField('טלפון3', max_length=100, help_text='טלפון נוסף, כולל קידומת')
    notes = models.TextField('הערות כלליות', max_length=1000, help_text="טקסט חופשי")

    class Meta:
        ordering = ["last_name","first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular person instance.
        """
        return reverse('person-detail', args=[str(self.id)])

    def get_gender(self):
        if self.gender == self.GENDER[0][0]:
            return self.GENDER[0][1]
        else:
            return self.GENDER[1][1]

    def get_str_for_pdf(self):
        """
        String for representing the Model object for PDF report
        """
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(
            self.last_name,
            self.first_name,
            self.get_gender(),
            str(self.id_num)[::-1],
            str(self.date_of_birth)[::-1],
            str(self.age)[::-1],
            self.address,
            self.city,
            str(self.phone1)[::-1],
            str(self.phone2)[::-1],
            str(self.phone3)[::-1],
            self.notes)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(
            self.last_name,
            self.first_name,
            self.get_gender(),
            self.id_num,
            self.date_of_birth,
            self.age,
            self.address,
            self.city,
            self.phone1,
            self.phone2,
            self.phone3,
            self.notes)
