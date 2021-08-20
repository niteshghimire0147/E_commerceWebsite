from re import I
from carts.models import Review
from django import forms
from django.forms import Form
from django.forms import ModelForm

PAYMENT_CHOICES = (
    ('E', 'Esewa'),
    ('K', 'Khalti'),
    ('I', 'Imepay'),
)


class CheckoutForm(forms.Form):
    shipping_first_name = forms.CharField(max_length=50)
    shipping_last_name = forms.CharField(max_length=50)
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = forms.CharField(max_length=50)
    shipping_zip = forms.CharField(required=False)
    shipping_phone_number = forms.IntegerField()
    shipping_gmail = forms.EmailField(max_length=50)

    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','rate']
