from rest_framework.routers import DefaultRouter
from .viewsets import CourseViewSet

router = DefaultRouter()
router.register(r"course", CourseViewSet)