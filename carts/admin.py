from django.contrib import admin

# Register your models here.
from .models import Review,Item, OrderItem, Order, Payment, Coupon, Refund, Address, Category,Brand,UserProfile


# Register your models here.

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'product',
                    'comment',
                    'rate',
                    'created_at'
                    ]
    readonly_fields= ['created_at',]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'street_address',
        'apartment_address',
        'phone_number',
        'country',
        'gmail',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country','gmail','first_name','last_name']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip','phone_number']

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)

admin.site.register(Address, AddressAdmin)
