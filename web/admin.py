from django.contrib import admin
from web.models import AddJob
from web.models import Category
from web.models import Certificate
from web.models import Client
from web.models import Contact
from web.models import Gallery
from web.models import JobApplication
from web.models import Partner
from web.models import Product
from web.models import ProductOrder
from web.models import Project
from web.models import Service
from web.models import Testimonial


# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "review")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "subject")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "item", "phone")


@admin.register(AddJob)
class AddJobAdmin(admin.ModelAdmin):
    list_display = ("job_title", "job_type")
    prepopulated_fields = {"slug": ("job_title",)}


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "name", "email")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name",)
