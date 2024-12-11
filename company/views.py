from django.shortcuts import render
from django.http import HttpResponse
from .models import Branches,Departments

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