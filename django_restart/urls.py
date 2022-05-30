from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_1/', include('lesson_1.urls')),
    path('lesson_2/', include('lesson_2.urls')),
    path('lesson_3/', include('lesson_3.urls')),
    path('lesson_5/', include('lesson_5.urls')),
    path('lesson_7/', include('lesson_7.urls')),
    path('lesson_8/', include('lesson_8.urls')),
    
]

