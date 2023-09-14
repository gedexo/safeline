import json

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from web.models import (
    Blog,
    Category,
    Certificate,
    Client,
    Gallery,
    Partner,
    Product,
    Project,
    Service,
    Testimonial,
)

from .forms import ContactForm, JobApplicationsForm, ProductEnquiryForm

# Create your views here.


def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    blogs = Blog.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    partners = Partner.objects.all()

    context = {
        "services": services,
        "projects": projects,
        "blogs": blogs,
        "testimonials": testimonials,
        "clients": clients,
        "is_index": True,
        "partners": partners,
    }

    return render(request, "index.html", context)


def about(request):
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    context = {"testimonials": testimonials, "clients": clients, "is_about": True}
    return render(request, "about.html", context)


def services(request):
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    clients = Client.objects.all()
    partners = Partner.objects.all()

    context = {
        "services": services,
        "is_services": True,
        "testimonials": testimonials,
        "clients": clients,
        "partners": partners,
    }
    return render(request, "services.html", context)


def services_details(request, slug):
    services = Service.objects.get(slug=slug)
    context = {"services": services, "is_services": True}
    return render(request, "servicedetails.html", context)


def projects(request):
    projects = Project.objects.all()
    partners = Partner.objects.all()
    gallery = Gallery.objects.all()

    context = {
        "projects": projects,
        "is_projects": True,
        "partners": partners,
        "gallery": gallery,
    }
    return render(request, "projects.html", context)


def blogs(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs, "is_blog": True}

    return render(request, "blogs.html", context)


def blog_detail(request, slug):
    blogs = Blog.objects.get(slug=slug)
    recent_blogs = Blog.objects.all()[:3]
    context = {"blogs": blogs, "recent_blogs": recent_blogs, "is_blog": True}

    return render(request, "blog-single.html", context)


def contact(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)

            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {"form": form, "is_contact": True}
    return render(request, "contact.html", context)


def products_category(request):
    categories = Category.objects.all()
    print(categories)
    context = {"categories": categories, "is_product": True}
    return render(request, "product.html", context)


def products_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    print(products)
    context = {"products": products, "is_product": True}
    return render(request, "product-list.html", context)


def products_single(request, slug):
    product_detail = Product.objects.get(slug=slug)
    form = ProductEnquiryForm(
        item=product_detail.name, data=request.POST or None, files=request.FILES or None
    )
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            email = form.cleaned_data["email"]
            send_product_mail(data, email)

            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    context = {"product_detail": product_detail, "is_product": True, "form": form}
    return render(request, "products-single.html", context)


def send_product_mail(data, email):
    text_content = "welcome"
    to_address = ("enquiry@safe-line.co",)
    from_email = email
    subject = "New Product Enquiry"
    template_context = {"data": data}
    html_content = render_to_string("email-template.html", template_context)

    kwargs = dict(
        to=to_address,
        from_email=from_email,
        subject=subject,
        body=strip_tags(text_content),
        alternatives=((html_content, "text/html"),),
    )
    message = EmailMultiAlternatives(**kwargs)
    message.attach_file(data.attachments.path)
    message.send()


def careers(request):
    form = JobApplicationsForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            email = form.cleaned_data["email"]
            send_mail(data, email)
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    context = {"is_career": True, "form": form}
    return render(request, "careers.html", context)


def send_mail(data, email):
    text_content = "welcome"
    to_address = ("careers.safeline@gmail.com",)
    from_email = email
    subject = "New Application"
    template_context = {"data": data}
    html_content = render_to_string("email-templateapplication.html", template_context)

    kwargs = dict(
        to=to_address,
        from_email=from_email,
        subject=subject,
        body=strip_tags(text_content),
        alternatives=((html_content, "text/html"),),
    )
    message = EmailMultiAlternatives(**kwargs)
    message.attach_file(data.resume.path)
    message.send()


def certificates(request):
    certificate = Certificate.objects.all()
    context = {"is_certificate": True, "certificate": certificate}
    return render(request, "certificates.html", context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {"is_gallery": True, "gallery": gallery}
    return render(request, "gallery.html", context)
