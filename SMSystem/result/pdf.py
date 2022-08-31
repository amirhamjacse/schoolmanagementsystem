from io import BytesIO
from re import template
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from academic.models import Subject, Student

def render_to_pdf(template_src, context_dic={}):
    template=get_template(template_src)
    html=template.render(context_dic)
    result = BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO--8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def pdfres(request, id):
    pi = Student.objects.get(pk=id)
    try:
        ps = Subject.objects.get(std=id)
    except Subject.DoesNotExist:
        ps = None
    a = Subject.objects.all()
    context={'s':pi, 'ps':ps}
    pdf = render_to_pdf('result/detailsres.html', context)
    if pdf:
        response=HttpResponse(pdf, content_type="application/pdf")
        content = "inline; filename=result.pdf"
        response['Content-Disposition']=content
        return response
    return HttpResponse("Not Found")
