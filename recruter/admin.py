from django.contrib import admin
from .models import JobPosting






class JobAdmin(admin.ModelAdmin):
    list_display=['id','job_title','job_type','salary']
    
admin.site.register(JobPosting,JobAdmin)