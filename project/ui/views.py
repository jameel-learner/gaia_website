from django.shortcuts import render
from django.template.loader import get_template, render_to_string


# Create your views here.
from helper.views import load_request_data
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages


def homepage(request):
    print("reached quality")
    context = {
        'on_page': 'homepage'
    }
    return render(request, 'index.html', context)


def contact_us(request):
    print("reached contact_us")
    if request.method == 'POST':
        form_data = {}
        html_form_fields = [
            'name', 'email', 'subject', 'message', 'mobile_number',
        ]
        # upload_file_fields = ['id_proof_img_all', 'pass_photo_all']
        load_request_data(form_data, html_form_fields, request, 'FORM')
        # load_request_data(form_data, upload_file_fields, request, 'FILE')
        print(form_data)
        # ContactUsDetails.objects.create(email=email,subject=subject,message=message,name =name,mobile_number = mobile_number)

        try:
            html_content = render_to_string('contact_us_email_template.html', {
                'name': form_data['name'], 'email': form_data['email'], 'subject': form_data['subject'],
                'message': form_data['message'], 'mobile_number': form_data['mobile_number']})
            to_email = settings.DEFAULT_CONTACT.split(",")
            print(f"to_email : {to_email} ")
            msg = EmailMessage('Contact Us', html_content, to=to_email)          # [to_email, ])
            msg.content_subtype = 'html'
            msg.send()

        except Exception as e:
            print(e)
            pass

        messages.success(request, 'Your valuable comments have reached us. We will get back to you soon...')


    context = {
        'on_page': 'contact_us'
    }
    return render(request, 'contact.html', context)


def about_us(request):
    print("reached about_us")
    context = {
        'on_page': 'about_us'
    }
    return render(request, 'about_us.html', context)


def management(request):
    print("reached management")
    context = {
        'on_page': 'management'
    }
    return render(request, 'management.html', context)


def services(request, number):
    print(f"reached services : {number}")
    context = {
        'on_page': 'services'
    }
    if number == 1:
        return render(request, 'services_procurement.html', context)
    elif number == 2:
        return render(request, 'services_design.html', context)
    elif number == 3:
        return render(request, 'services_quality.html', context)
    elif number == 4:
        return render(request, 'services_sales.html', context)
    elif number == 5:
        return render(request, 'services_compliance.html', context)
    elif number == 6:
        return render(request, 'services_inventory.html', context)

    return render(request, 'services.html', context)


def quality(request):
    print("reached quality")
    context = {
        'on_page': 'quality'
    }
    return render(request, 'quality.html', context)


def crm(request):
    print("reached quality")
    context = {
        'on_page': 'search_crm'
    }
    return render(request, 'search_crm.html', context)
