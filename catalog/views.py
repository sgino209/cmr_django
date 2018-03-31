# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Views creation
# (A view is a function that processes an HTTP request, fetches data from the database as needed, generates an HTML page
#  by rendering this data using an HTML template, and then returns the HTML in an HTTP response to be shown to the user)

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person
import csv
from django.core.exceptions import PermissionDenied
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.http import HttpResponse
from smsish.sms import send_sms
from smsish.sms.message import SMSMessage

pdfmetrics.registerFont(TTFont('Hebrew', 'ArialHB.ttf'))

def index(request):
    """ View function for home page of site """

    # Generate counts of some of the main objects
    num_persons=Person.objects.count()
    num_males = Person.objects.filter(gender__exact='m').count()
    num_females = Person.objects.filter(gender__exact='f').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_persons':num_persons,
                 'num_males':num_males,
                 'num_females':num_females,
                 'num_visits':num_visits}
    )

def PersonExportCsvView(request):

    queryset = Person.objects.all()

    if not request.user.is_staff:
        raise PermissionDenied

    opts = queryset.model._meta
    model = queryset.model

    # Force download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=export.csv'

    # The csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]

    # Write a first row with header information
    writer.writerow(field_names)

    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return HttpResponse(response, content_type='text/csv')

def PersonExportPdfView(request):
    # Create the HttpResponse object with the appropriate PDF headers.

    queryset = Person.objects.all()

    if not request.user.is_staff:
        raise PermissionDenied

    opts = queryset.model._meta
    model = queryset.model

    # Force download
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="export.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    field_names = [field.name for field in opts.fields]
    field_names_str = ', '.join(field_names)
    N = 800
    p.drawString(10, N, field_names_str)
    N -= 30
    p.setFont("Hebrew", 14)
    for obj in queryset:
        p.drawString(10, N, str(obj.get_str_for_pdf())[::-1].encode('utf-8'))
        N -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def PersonSendSmsView(request):
    TWILIO_MAGIC_FROM_NUMBER = "+15005550006"
    VALID_FROM_NUMBER = TWILIO_MAGIC_FROM_NUMBER
    VALID_TO_NUMBER = TWILIO_MAGIC_FROM_NUMBER
    sms = SMSMessage(
        "Body",
        VALID_FROM_NUMBER,
        [VALID_TO_NUMBER]
    )
    sms.send()

    send_sms("Body", VALID_FROM_NUMBER, [VALID_TO_NUMBER])

    return render(request, 'sms_sent.html')

class PersonListView(generic.ListView):
    """ Generic class-based list view for a list of persons. """
    model = Person
    paginate_by = 10 

class PersonDetailView(generic.DetailView):
    """ Generic class-based detail view for a person. """
    model = Person

class PersonCreate(PermissionRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class PersonUpdate(PermissionRequiredMixin, UpdateView):
    model = Person
    #fields = ['gender','id_num','first_name','last_name','date_of_birth','age','address','city','phone1','phone2','phone3','notes']
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class PersonDelete(PermissionRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('persons')
    permission_required = 'catalog.can_mark_returned'
