from django.contrib import admin
from .models import Artwork, Enquiry


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'artwork', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
