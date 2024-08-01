from django.shortcuts import render,redirect
from app1.forms import MarksForm
from app1.models import Marks
# Create your views here.
def view_index(request):
    return render(request,"app1/index.html",context={})
def list_marks(request):
    marks_data=Marks.objects.all()
    return render(request,"app1/list_marks.html",context={'marks_data':marks_data})
def add_view(request):
    if request.method=="GET":
        form=MarksForm()
        return render(request,"app1/add_stud.html",context={'form':form})
    elif request.method=="POST":
        form=MarksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=MarksForm()
            return render(request,"app1/add_stud.html",context={'form':form})
        else:
            return render(request,"app1/add_stud.html",context={'form':form})
def edit_view(request,id):
    if request.method=="GET":
        stud=Marks.objects.get(id=id)
        form=MarksForm(instance=stud)
        return render(request,"app1/update_stud.html",context={'form':form})
    elif request.method=="POST":
        stud=Marks.objects.get(id=id)
        form=MarksForm(request.POST,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            return redirect("update")

        else:
            return render(request,"app1/update_stud.html",context={'form':form})
def search_view(request):
    return render(request,"app1/search.html",context={})
def find_view(request):
    rollno=request.GET.get("rollno")
    try:
        stud=Marks.objects.get(rollno=rollno)
        found=True
        return render(request,"app1/search.html",context={'stud':stud,'found':found})
    except:
        return render(request,"app1/search.html",context={'msg':"InvalidRollno"})
def find_result(request):
    marks_qs=Marks.objects.all()
    marks_list=[]
    for stud in marks_qs:
        row=[stud.rollno,stud.name,stud.subject1,stud.subject2,stud.subject3]
        row.append(stud.subject1+stud.subject2+stud.subject3)
        rs="PASS" if stud.subject1>=40 and stud.subject2>=40 and stud.subject3>=40 else "FAIL"
        row.append(rs)
        marks_list.append(row)
    return render(request,"app1/result.html",context={"marks_list":marks_list})