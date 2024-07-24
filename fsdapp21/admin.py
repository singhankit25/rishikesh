from django.contrib import admin

from fsdapp21.models import Student,Course

# Register your models here.

#admin.site.register(student)
#admin.site.register(course)

admin.site.site_header='FDP ON Django'
admin.site.site_title='FDP ON Django'

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
  list_display=('usn','name')
  ordering=('usn',)
  search_fields=('name',)

@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
  list_display=('courseCode','courseName')
  ordering=('courseCode',)
  search_fields=('courseName',)