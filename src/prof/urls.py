from django.urls import path
from .views import (
    ProfListView,
    ProfDetailView,
    TestUpdateView,
    TestimonialCreateView,
    StudentTestimonialListView
)

app_name = 'prof'
urlpatterns = [
    path('', ProfListView.as_view(), name='prof-list'),
    path('<int:id>/create/', TestimonialCreateView.as_view(), name='test-create'),
    path('<int:id>/', ProfDetailView.as_view(), name='prof-detail'),
    path('<int:id>/update/',
         TestUpdateView.as_view(), name='test-update'),
    path('my-testimonials/', StudentTestimonialListView.as_view(),
         name='student-testimonials')
]
