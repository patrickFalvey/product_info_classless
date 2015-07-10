from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, render
##from .email_image import email_embed_image
from email.MIMEImage import MIMEImage
from .forms import EmailForm
from .FFLMail import sendproduct
from .models import Product
##from vArmory import settings

def home(request):
    form = ProductInfoEmailForm(request.POST or None)   
    context = {"form": form}
    template = "saas_app/product-search-result.html"   
    if form.is_valid():
        to_email = [form.cleaned_data['Customer_email']]
        subject = "Product that you had expressed interest in."
        body = "  Here are the details for the item we've discussed.  There's a limited quantity available, so let me know when you are ready to place your order."
        html_content = render_to_string('saas_app/email/product_info_email.html', context)
        msg = EmailMultiAlternatives(subject, body,
                             'patrickfalvey40@gmail.com', to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.mixed_subtype = 'related'
        img_content_id = 'gun'
        img_data = open(product.image_url(), 'rb')
        msg_img = MIMEImage(img_data.read())
        img_data.close()
        msg_img.add_header('Content-ID', '<{}>'.format(product.picture))
        msg.attach(msg_img)
        msg.send()        

    return render(request, template, context)



