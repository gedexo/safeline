from django.urls import path

from . import views


app_name = "web"


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("services-details/<slug>/", views.services_details, name="services-details"),
    path("projects", views.projects, name="projects"),
    path("blogs", views.blogs, name="blogs"),
    path("blog-detail/<slug>/", views.blog_detail, name="blog-detail"),
    path("contact", views.contact, name="contact"),
    path("products-category", views.products_category, name="products-category"),
    path("products-list/<slug>/", views.products_list, name="products-list"),
    path("products-single/<slug>", views.products_single, name="products-single"),
    path("careers", views.careers, name="careers"),
    path("certificates", views.certificates, name="certificates"),
    path("gallery", views.gallery, name="gallery"),
]
