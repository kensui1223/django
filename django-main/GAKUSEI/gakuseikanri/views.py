from django.shortcuts import render
from django.shortcuts import render, redirect
from .Forms import StudentForm
from .models import Student

def gsk(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
def show(request):
    students = Student.objects.all()
    return render(request,"show.html",{'students':students})
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request,"edit.html",{'student':student})
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'student':student})
def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")

def search(request, student_id):
    student = Student.objects.all.filter(student_id=student_id)
    return render(request, "search.html",{'student':student})