import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import StudentForm  
from .models import student   

#===ADD STUDENT===#

def addstudent(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        date_of_birth = request.POST.get('dob')
        department = request.POST.get('department')
        program = request.POST.get('program')
        level = request.POST.get('level')

        # Validate form data
        if not all([first_name, last_name, email, contact, date_of_birth, department, program, level]):
            messages.error(request, "All fields are required.")
            return redirect('addstudent')

        # Convert date_of_birth to date object
        try:
            date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
            return redirect('addstudent')

        # Check if email is unique
        if student.objects.filter(email=email).exists():  
            messages.error(request, "Email already exists.")
            return redirect('addstudent')

        # Create and save the student
        student1 = student(  
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            date_of_birth=date_of_birth,
            department=department,
            program=program,
            level=level
        )
        student1.save()
        messages.success(request, "Student added successfully.")
        return redirect('allstudents')

    return render(request, 'addstudent.html', {})

#===ALL STUDENTS===#

def allstudents(request):
    all_students = student.objects.all()  # Corrected model name
    return render(request, 'allstudents.html', {'students': all_students})

#===STUDENT DASHBOARD===#

def dashboard(request):
    total_students = student.objects.count()  

    context = {
        'total_students': total_students
    }
    return render(request, 'dashboard.html', context)

#===EDIT STUDENT===#

def edit(request, id):
    student1 = get_object_or_404(student, id=id)  
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student1)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('allstudents')
    else:
        form = StudentForm(instance=student1)
    return render(request, 'edit.html', {'form': form})

#===DELETE STUDENT===#

def delete(request, id):
    student1 = get_object_or_404(student, id=id) 
    if request.method == 'POST':
        student1.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('allstudents')
    return render(request, 'delete.html', {'student': student1})

#===REGISTER STUDENT===#

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if user with the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "You are now registered and can log in.")
        return redirect('login')

    return render(request, 'authenticate/register.html', {})

#===LOGIN STUDENT===#

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

