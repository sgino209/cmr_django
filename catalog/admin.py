# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Models registration

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

class PersonAdmin(ImportExportModelAdmin):
    """
    Administration object for Person models.
    Defines:
     - list_display --> fields to be displayed in list view (list_display)
     - fields --> orders fields in detail view (form), can be grouped horizontally as tuples
    """
    list_display = ('id_num','last_name','first_name','gender','date_of_birth','age','address','city','phone1','phone2','phone3','notes')
    #fields = ['id_num','last_name','first_name','gender','date_of_birth','age','address','city','phone1','phone2','phone3','notes']
    fieldsets = (
        ('פרטיים אישיים', {
            'fields': ('id_num', 'last_name', 'first_name', 'gender', 'date_of_birth', 'age')
        }),
        ('כתובת', {
            'fields': ('address', 'city')
        }),
        ('דרכי התקשרות', {
            'fields': ('phone1', 'phone2', 'phone3')
        }),
        ('הערות', {
            'fields': ('notes',)
        }),
    )

admin.site.register(Person, PersonAdmin)

