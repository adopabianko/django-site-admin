from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'grade', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]