import zipfile
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
from urllib.parse import quote


def render_to_pdf(template_src, d, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        response = HttpResponse(
            result.getvalue(), content_type='application/pdf')
        raw_filename = f"{d.pk} {d.donor.donor_name}.pdf"
        safe_filename = quote(raw_filename)
        response['Content-Disposition'] = (
            f'attachment; filename="{raw_filename}"; filename*=UTF-8\'\'{safe_filename}'
        )
        return response
    return None


def generate_zip(pdf_array, pdf_array_names):
    # Open HttpResponse
    response = HttpResponse(content_type='application/zip')
    # Get date
    today = timezone.localdate()
    today_date = str(today.year) + "-" + \
        str(today.month) + "-" + str(today.day)
    # Set correct content-disposition
    zip_name = 'Tax Receipts ' + today_date + '.zip'
    response['Content-Disposition'] = 'attachment; filename=' + zip_name
    # Open the file, writable
    zip = zipfile.ZipFile(response, 'w')

    idx = 0
    for name in pdf_array_names:
        zip.writestr(name, pdf_array[idx].getvalue())
        idx += 1

    # Must close zip for all contents to be written
    zip.close()

    return response
