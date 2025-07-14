from django.contrib import admin

# Register your models here.
from .models import Professor, Testimonial
admin.site.register(Professor)
admin.site.register(Testimonial)
