from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service_type', 'status', 'created_at')
    list_filter = ('status', 'service_type')
    search_fields = ('customer__username', 'description')
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(status='Resolved')
    mark_resolved.short_description = "Mark selected requests as Resolved"
