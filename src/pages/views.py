from django.shortcuts import render, redirect

# Create your views here.


def landing_page(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        if student_name:
            request.session['student_name'] = student_name
            return redirect('prof:prof-list')  # redirect to professor list
    return render(request, 'home.html')
