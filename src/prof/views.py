from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
)
from .models import Professor, Testimonial
from .forms import TestimonialModelForm


class ProfListView(ListView):
    template_name = 'prof/prof_list.html'
    queryset = Professor.objects.all()


class ProfDetailView(DetailView):
    model = Professor  # ❗️Ensure this is Professor, not Testimonial
    template_name = 'prof/prof_detail.html'
    context_object_name = 'professor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = self.object.testimonials.all()
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Professor, id=id_)


class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialModelForm
    template_name = 'prof/prof_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.professor = get_object_or_404(Professor, id=kwargs['id'])
        self.student_name = request.session.get('student_name')
        # ✅ Check if testimonial already exists
        existing_testimonial = Testimonial.objects.filter(
            professor=self.professor,
            student_name=self.student_name
        ).first()

        if existing_testimonial:
            return redirect('prof:test-update', id=self.professor.id)

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        student_name = self.request.session.get('student_name')
        if student_name:
            initial['student_name'] = student_name
        return initial

    def form_valid(self, form):
        form.instance.student_name = self.request.session.get('student_name')
        messages.success(self.request, "Thanks for submitting!")
        form.instance.professor = self.professor
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('prof:prof-detail', kwargs={'id': self.professor.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professor'] = self.professor
        return context


class TestUpdateView(UpdateView):
    model = Testimonial
    form_class = TestimonialModelForm
    template_name = 'prof/prof_create.html'

    def get_object(self):
        professor_id = self.kwargs.get("id")
        student_name = self.request.session.get('student_name')

        if not student_name:
            raise PermissionDenied("No student name in session.")

        return get_object_or_404(
            Testimonial,
            professor__id=professor_id,
            student_name=student_name
        )

    def form_valid(self, form):
        messages.success(self.request, "Your testimonial has been updated.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('prof:prof-detail', kwargs={'id': self.object.professor.id})


class StudentTestimonialListView(ListView):
    model = Testimonial
    template_name = 'prof/student_testimonials.html'
    context_object_name = 'testimonials'

    def get_queryset(self):
        student_name = self.request.session.get('student_name')
        if student_name:
            return Testimonial.objects.filter(student_name=student_name)
        return Testimonial.objects.none()
