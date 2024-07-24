"""
URL configuration for fsdproj21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from fsdapp21.views import (generateCSV, home, registerajax, studentlist, courselist, register, enrolledStudents, add_project, StudentListView, StudentDetailView, generatePDF, enrolledlistajax)
# urlpatterns = [
#  path('admin/', admin.site.urls),
#  path('', home, name='home'), # Root URL redirects to home
#  path('home/', home, name='home'),
#  path('studentlist/', studentlist, name='student_list'),
#  path('courselist/', courselist, name='course_list'),
#  path('register/', register, name='register'),
#  path('enrolledlist/', enrolledStudents, name='enrolled_students'),
#  path('addproject/', add_project, name='add_project'),
#  path('genericlistviewstudent/', StudentListView.as_view(), name='student_list_view'),
#  path('genericdetailedviewstudent/<int:pk>/', StudentDetailView.as_view(), name='student_detail_view'),
#  path('download_course_table_as_csv/', generateCSV, name='download_course_csv'),
#  path('download_course_table_as_pdf/', generatePDF, name='download_course_pdf'),
#  path('courseRegUsingAjax/', registerajax, name='register_ajax'),
#  path('course_search_ajax/', enrolledlistajax, name='enrolled_list_ajax'),
# ]

from django.contrib import admin
from django.urls import path
from fsdapp21.views import (
    generateCSV, home, registerajax, studentlist, courselist, 
    register, enrolledStudents, add_project, StudentListView, 
    StudentDetailView, generatePDF, enrolledlistajax
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL redirects to home
    path('home/', home, name='home'),
    path('studentlist/', studentlist, name='student_list'),
    path('courselist/', courselist, name='course_list'),
    path('register/', register, name='register'),
    path('enrolledlist/', enrolledStudents, name='enrolled_students'),
    path('addproject/', add_project, name='add_project'),
    path('genericlistviewstudent/', StudentListView.as_view(), name='student_list_view'),
    path('genericdetailedviewstudent/', StudentDetailView.as_view(), name='student_detail_view'),
    path('download_course_table_as_csv/', generateCSV, name='download_course_csv'),
    path('download_course_table_as_pdf/', generatePDF, name='download_course_pdf'),
    path('courseRegUsingAjax/', registerajax, name='register_ajax'),
    path('course_search_ajax/', enrolledlistajax, name='enrolled_list_ajax'),
]


