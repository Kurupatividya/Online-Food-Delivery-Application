from django.shortcuts import render,redirect
from django.views import View
from .models import MEMBERSHIP
from .forms import AddEmployeeForm
# Create your views here.

class FirstPage(View):
    def get(self,request):
        return render(request,'SecuritySystem/firstpage.html')

class FeedBack(View):
    def get(self,request):
        return render(request,'SecuritySystem/feedback.html')

class Home(View):
    def get(self,request):
        studata = MEMBERSHIP.objects.all()
        return render(request,'SecuritySystem/home.html',{'studata':studata})

class AddEmployee(View):
    def get(self,request):
        fm = AddEmployeeForm()
        return render(request,'SecuritySystem/AddEmployee.html',{'form':fm})
    def post(self,request):
        fm = AddEmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Home')
        else:
            return render(request, 'SecuritySystem/AddEmployee.html', {'form': fm})

class DeleteEmployee(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        studata = MEMBERSHIP.objects.get(id=id)
        studata.delete()
        return redirect('/Home')

class EditEmployee(View):
    def get(self,request,id):
        stu = MEMBERSHIP.objects.get(id=id)
        fm = AddEmployeeForm(instance=stu)
        return render(request,'SecuritySystem/EditEmployee.html',{'form':fm})
    def post(self,request,id):
        stu = MEMBERSHIP.objects.get(id=id)
        fm = AddEmployeeForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/Home')