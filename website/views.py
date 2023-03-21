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
    return render(request, 'sgaia_index.html', context)


def contact_us(request, service_name):
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
        'on_page': 'contact_us',
        'service_name': service_name,
    }
    return render(request, 'sgaia_contact_us.html', context)


def about_us(request):
    print("reached about_us")
    context = {
        'on_page': 'about_us'
    }
    return render(request, 'sgaia_about_us.html', context)


def history_all(request):
    print("reached history_all")
    context = {
        'on_page': 'history_all'
    }
    return render(request, 'sgaia_history.html', context)


def history(request, service_name):
    print("reached history")
    context = {
        'on_page': 'history',
        'service_name': service_name,
    }
    return render(request, 'sgaia_history_details.html', context)


def strategy(request):
    print("reached strategy")
    context = {
        'on_page': 'strategy'
    }
    return render(request, 'sgaia_strategy.html', context)


def md_message(request):
    print("reached md_message")
    context = {
        'on_page': 'md_message'
    }
    return render(request, 'sgaia_md_message.html', context)


def team(request, team_name):
    print("reached team")
    context = {
        'on_page': 'team',
        'team_name': team_name,
    }
    return render(request, 'sgaia_team_details.html', context)


def business(request, service_name):
    number = '34'
    print(f"reached services : {number}")
    context = {
        'on_page': 'services',
        'service_name': service_name,
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

    return render(request, 'sgaia_service_details.html', context)


def partnering(request, service_name):
    print("reached partnering")
    context = {
        'on_page': 'partnering',
        'service_name': service_name,
    }
    return render(request, 'sgaia_partner_details.html', context)


def product(request, pid, product_name):
    print("reached product")
    context = {
        'on_page': 'product',
        'pid': pid,
        'product_name': product_name,
    }
    return render(request, 'sgaia_product.html', context)


def shop_all(request, category):
    print("reached shop_all")
    context = {
        'on_page': 'shop_all',
        'category': category,
    }
    return render(request, 'sgaia_shop_all.html', context)


def shop(request):
    print("reached shop")
    context = {
        'on_page': 'shop'
    }
    return render(request, 'sgaia_shop.html', context)


def media_all(request):
    print("reached media_all")
    context = {
        'on_page': 'media_all'
    }
    return render(request, 'sgaia_media.html', context)


def media(request, mtitle):
    print("reached media")
    context = {
        'on_page': 'media',
        'mtitle': mtitle,
    }
    return render(request, 'sgaia_media_details.html', context)
