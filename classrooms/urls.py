
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app2.views import ListAPIView

from classes import views
from app2 import views as views2
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    
    path('list/', views2.ClassListView.as_view(), name='list'),
    path('detail/<int:classroom_id>/', views2.ClassDetailView.as_view(), name='detail'),
    path('create/', views2.ClassCreateView.as_view(), name='create'),
    path('<int:classroom_id>/update/', views2.ClassUpdateView.as_view(), name='update'),
    path('<int:classroom_id>/delete/', views2.ClassDeleteView.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login')
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
