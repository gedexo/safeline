# Generated by Django 4.2.5 on 2023-10-05 12:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=500)),
                ('job_Category', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
                ('about_job', tinymce.models.HTMLField(blank=True, null=True)),
                ('basic_requirements', tinymce.models.HTMLField(blank=True, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb_image', versatileimagefield.fields.VersatileImageField(upload_to='blog/', verbose_name='Thumbnail Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('cover_image', versatileimagefield.fields.VersatileImageField(upload_to='blog/', verbose_name='Cover Image')),
                ('title', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('content_sec1', tinymce.models.HTMLField(blank=True, null=True)),
                ('quote', models.TextField(blank=True, null=True)),
                ('quote_author', models.CharField(max_length=200)),
                ('content_sec2', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='category/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name=' Title')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='clients/', verbose_name='Certificate Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='clients/', verbose_name='Client Logo')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name=' Title')),
                ('thumb_image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Thumbnail Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Full Size Image')),
                ('note', models.TextField(blank=True, null=True)),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('resume', models.FileField(upload_to='Job Applications/')),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Partner/', verbose_name='Product Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('partner_logo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='Partner/', verbose_name='Partner Logo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('note', models.TextField()),
                ('attachments', models.FileField(blank=True, help_text='Optional: Attach any additional files if needed.', null=True, upload_to='Attachments/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Project/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('client_logo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='Project/', verbose_name='Client Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Service/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('imagetwo', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='Service/', verbose_name='Image 2')),
                ('sub_heading', models.TextField(blank=True, null=True)),
                ('heading', models.TextField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('description_two', tinymce.models.HTMLField(blank=True, null=True)),
                ('sub_head', models.TextField(blank=True, null=True)),
                ('sub_content', tinymce.models.HTMLField(blank=True, null=True)),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
                ('meta_title', models.CharField(max_length=500)),
                ('meta_description', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='testimonial/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('review', tinymce.models.HTMLField(blank=True, null=True)),
                ('place', models.TextField(blank=True, null=True, verbose_name='Place or Designation')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='product/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('about_product', tinymce.models.HTMLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='web.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
