from django.db import models
from django.urls import reverse

# Create your models here.


class Professor(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("prof:prof-detail", kwargs={'id': self.id})


class Testimonial(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="testimonials")
    student_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.student_name} for Prof. {self.professor.name}"
    
    class Meta:
        unique_together = ('professor', 'student_name')  # ✅ Prevent duplicate testimonials
    
    def get_absolute_url(self):
        return reverse('prof:prof-detail', kwargs={'id': self.professor.id})
