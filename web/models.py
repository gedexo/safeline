from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


class Service(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    image = VersatileImageField("Image", upload_to="Service/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    imagetwo = VersatileImageField(
        "Image 2", upload_to="Service/", ppoi_field="ppoi", null=True, blank=True
    )
    sub_heading = models.TextField(null=True, blank=True)

    heading = models.TextField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    description_two = HTMLField(null=True, blank=True)
    sub_head = models.TextField(null=True, blank=True)
    sub_content = HTMLField(null=True, blank=True)

    order = models.CharField(max_length=10, null=True, blank=True)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["order"]


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    image = VersatileImageField("Image", upload_to="Project/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    client_logo = VersatileImageField(
        "Client Logo", upload_to="Project/", ppoi_field="ppoi", null=True, blank=True
    )

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    thumb_image = VersatileImageField(
        "Thumbnail Image", upload_to="blog/", ppoi_field="ppoi"
    )
    ppoi = PPOIField("Image PPOI")
    cover_image = VersatileImageField(
        "Cover Image", upload_to="blog/", ppoi_field="ppoi"
    )

    title = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.CharField(max_length=200)
    date = models.DateField()
    content_sec1 = HTMLField(null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    quote_author = models.CharField(max_length=200)
    content_sec2 = HTMLField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="testimonial/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    review = HTMLField(null=True, blank=True)
    place = models.TextField("Place or Designation", null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Client(models.Model):
    name = models.CharField("Company Name", max_length=100, null=True, blank=True)
    image = VersatileImageField("Client Logo", upload_to="clients/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    image = VersatileImageField(
        "Image", upload_to="category/", ppoi_field="ppoi", null=True, blank=True
    )
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = VersatileImageField(
        "Image", upload_to="product/", ppoi_field="ppoi", null=True, blank=True
    )

    ppoi = PPOIField("Image PPOI")
    about_product = HTMLField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    item = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    phone = PhoneNumberField()
    country = models.CharField(max_length=250)
    email = models.EmailField()
    note = models.TextField()
    attachments = models.FileField(
        upload_to="Attachments/",
        null=True,
        blank=True,
        help_text="Optional: Attach any additional files if needed.",
    )

    def __str__(self):
        return self.first_name


class AddJob(models.Model):
    CHOICES = (
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Internship", "Internship"),
        ("Remote", "Remote"),
    )

    job_title = models.CharField(max_length=500)
    job_Category = models.CharField(max_length=500)
    slug = models.SlugField(max_length=300, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    vacancy = models.IntegerField(blank=True, null=True)

    about_job = HTMLField(blank=True, null=True)
    basic_requirements = HTMLField(blank=True, null=True)
    job_type = models.CharField(max_length=100, choices=CHOICES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.job_title


class JobApplication(models.Model):
    job = models.TextField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = PhoneNumberField()
    resume = models.FileField(upload_to="Job Applications/")
    note = models.TextField()

    def __str__(self):
        return self.name + ": Job Applications for the Position of " + self.job


class Certificate(models.Model):
    name = models.CharField(" Title", max_length=100, null=True, blank=True)
    image = VersatileImageField(
        "Certificate Image", upload_to="clients/", ppoi_field="ppoi"
    )
    ppoi = PPOIField("Image PPOI")
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Partner(models.Model):
    name = models.CharField(max_length=255)

    image = VersatileImageField(
        "Product Image", upload_to="Partner/", ppoi_field="ppoi"
    )
    ppoi = PPOIField("Image PPOI")
    partner_logo = VersatileImageField(
        "Partner Logo", upload_to="Partner/", ppoi_field="ppoi", null=True, blank=True
    )

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    name = models.CharField(" Title", max_length=100, null=True, blank=True)
    thumb_image = VersatileImageField(
        "Thumbnail Image",
        upload_to="gallery/",
        ppoi_field="ppoi",
        null=True,
        blank=True,
    )
    ppoi = PPOIField("Image PPOI")
    image = VersatileImageField(
        "Full Size Image",
        upload_to="gallery/",
        ppoi_field="ppoi",
        null=True,
        blank=True,
    )
    note = models.TextField(null=True, blank=True)
    order = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Gallery"
        ordering = ["order"]

    def __str__(self):
        return str(self.name)
