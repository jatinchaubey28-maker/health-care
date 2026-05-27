
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from health.models import Department, DoctorDetail, AppointmentDetails, Queries

admin.site.site_header = _('HealthCare Admin')
admin.site.site_title = _('HealthCare Title')
admin.site.index_title = _('HealthCare Admin Control')

# 🔹 Department Admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_image_tag')

    def department_image_tag(self, obj):
        if obj.department_image:
            return format_html('<img src="{}" width="50" height="50"/>', obj.department_image.url)
        return "No Image"

    department_image_tag.short_description = 'Image'

class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'doctor_full_name',
        'department_name',
        'gender',
        'age',
        'email',
        'mobile_number',
        'city',
        'doctor_image'
    )
    search_fields = ('doctor_full_name', 'email', 'city')
    list_filter = ('gender', 'city', 'department_name')

    def doctor_image_tag(self, obj):
        if obj.doctor_image:
            return format_html('<img src="{}" width="50" height="50"/>', obj.doctor_image.url)
        return "No Image"

    doctor_image_tag.short_description = 'Image'

class AppointmentDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'doctor_name',
        'appointment_date',
        'appointment_time',
        'patient_email',
        'patient_mobile_number'
    )
    search_fields = ('patient_name', 'doctor_name', 'patient_email')
    list_filter = ('appointment_date',)

class QueriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone', 'message')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Department,DepartmentAdmin)  
admin.site.register(DoctorDetail,DoctorDetailsAdmin)
admin.site.register(AppointmentDetails, AppointmentDetailsAdmin)
admin.site.register(Queries, QueriesAdmin)