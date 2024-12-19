from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Branches,Departments
from .forms import departmentForm

# Create your views here.
def hellowWorldView(request):
    return HttpResponse("<h1>hello world</h1>")

# def BranchesList(request):
#     AllBranches = Branches.objects.all()
#     print(AllBranches)
#     htmlSTR = """
#         <table border='1'>
#             <tr>
#                 <th>name</th>
#                 <th>adress</th>
#                 <th>phone</th>
#                 <th>email</th>
#             <tr>
# """
#     for branche in AllBranches:
#         htmlSTR += f"""
#                     <tr>
#                         <td>{branche.name}</td>
#                         <td>{branche.address}</td>
#                         <td>{branche.phone}</td>
#                         <td>{branche.email}</td>
#                     </tr>
# """
#     htmlSTR += """
#         </table>
# """
#     return HttpResponse(htmlSTR)
def BranchesList(request):
    AllBranches = Branches.objects.all()
    return render(request,"branchesList.html",{"branches":AllBranches})

def BrancheDetails(request,branche_id):
    branche = Branches.objects.get(pk=branche_id)
    return render(request,"brancheDetails.html",{"branche":branche})

def addBranche(request):
    if request.method == 'POST':
        name = request.POST["brancheName"]
        address = request.POST["brancheAddress"]
        phone = request.POST["branchePhone"]
        email = request.POST["brancheEmail"]
        b = Branches(name=name,address=address,phone=phone,email=email)
        b.save()
        return redirect('BrachesList')
    return render(request,'addBranche.html')

def editBranche(request,branche_id):
    branche = Branches.objects.get(pk = branche_id)
    if request.method == 'POST':
        branche.name = request.POST["brancheName"]
        branche.address = request.POST["brancheAddress"]
        branche.phone = request.POST["branchePhone"]
        branche.email = request.POST["brancheEmail"]
        branche.save()
        return redirect('BrachesList')
    return render(request,'editBranche.html',{'b':branche})

def addDepartment(request,branche_id):
    b = Branches.objects.get(pk=branche_id)
    form= departmentForm
    if request.method == 'POST':
        form = departmentForm(request.POST)
        if form.is_valid():
            formDepartment = form.save(commit=False)
            formDepartment.branche = b
            formDepartment.save()
            return redirect('BrancheDetails',b.pk)
    return render(request,"addDepartment.html",{'form':form,'branche':b})