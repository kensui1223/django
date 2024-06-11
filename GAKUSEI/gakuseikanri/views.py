from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm, StudentSearchForm

def student_create(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/list')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'gakuseikanri/student_form.html',{'form':form}) 

def student_list(request):
    search_form = StudentSearchForm(request.GET or None)
    query = None
    students = Student.objects.all()
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            students = students.filter(
                Q(student_id__icontains=query) |
                Q(name__icontains=query) |
                Q(number__icontains=query) |
                Q(email__icontains=query)
            )
    return render(request, 'gakuseikanri/student_list.html', {
        'students':students,
        'search_form':search_form})

def student_edit(request, id):  
    student = Student.objects.get(id=student_id)  
    return render(request,'student_edit.html', {'student':student})  

def student_update(request, id):
    student = get_object_or_404(Student, student_id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'gakuseikanri/student_form.html', {'form': form}) 

def student_delete(request, id):  
    student = Student.objects.get(student_id=id)  
    if request.method == 'POST':
        student.delete()
        return redirect('/list')
    return render(request, 'gakuseikanri/student_confirm_delete.html', {'student': student})