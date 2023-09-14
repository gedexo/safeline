from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Contact
from .models import JobApplication
from .models import ProductOrder


class ContactForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget()
    )  # Set your default country code here

    class Meta:
        model = Contact
        exclude = ()
        widgets = {
            "name": TextInput(
                attrs={"type": "text", "name": "name", "placeholder": "Your Name*"}
            ),
            "email": EmailInput(
                attrs={"type": "email", "placeholder": "Your Email*", "name": "email"}
            ),
            "subject": TextInput(
                attrs={"name": "subject", "type": "text", "placeholder": "Subject*"}
            ),
            "message": Textarea(
                attrs={"name": "message", "id": "message", "placeholder": "Message*"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Update the phone field widget's attributes to set the placeholder
        self.fields["phone"].widget.attrs["placeholder"] = "Phone Number* "


class ProductEnquiryForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget()
    )  # Set your default country code here

    class Meta:
        model = ProductOrder
        exclude = ()
        widgets = {
            "first_name": TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "id": "name",
                    "placeholder": "First Name*",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "type": "text",
                    "name": "last_name",
                    "id": "surname",
                    "placeholder": "Last Name*",
                }
            ),
            "email": EmailInput(
                attrs={
                    "type": "email",
                    "placeholder": "Email*",
                    "id": "email",
                    "name": "email",
                }
            ),
            "country": TextInput(
                attrs={"type": "text", "placeholder": "Country*", "name": "country"}
            ),
            "item": TextInput(
                attrs={
                    "type": "text",
                    "readonly": "readonly",
                    "placeholder": "Item Selected*",
                    "name": "item",
                }
            ),
            "note": Textarea(
                attrs={
                    "placeholder": "Description*",
                    "name": "description",
                    "id": "description",
                }
            ),
            "attachments": FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                    "name": "attachments",
                    "placeholder": "Upload Attachments here",
                }
            ),
        }

    def __init__(self, item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["item"].initial = item

        self.fields["phone"].widget.attrs["placeholder"] = "Phone Number*"
        self.fields["phone"].widget.attrs["class"] = "form-control"


class JobApplicationsForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget()
    )  # Set your default country code here

    class Meta:
        model = JobApplication
        exclude = ()
        widgets = {
            "job": TextInput(
                attrs={
                    "name": "job",
                    "type": "text",
                    "placeholder": "Applying Position*",
                }
            ),
            "name": TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "id": "name",
                    "placeholder": "Name*",
                }
            ),
            "email": EmailInput(
                attrs={
                    "type": "email",
                    "placeholder": "Email*",
                    "id": "email",
                    "name": "email",
                }
            ),
            "note": Textarea(
                attrs={
                    "name": "note",
                    "type": "text",
                    "cols": "10",
                    "rows": "4",
                    "placeholder": " *Brief information of the applicant (Please Specify)",
                }
            ),
            "resume": FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                    "name": "resume",
                    "placeholder": "Upload CV/Resume here",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(JobApplicationsForm, self).__init__(*args, **kwargs)
        # Update the phone field widget's attributes to set the placeholder
        self.fields["phone"].widget.attrs["placeholder"] = "Phone Number* "
