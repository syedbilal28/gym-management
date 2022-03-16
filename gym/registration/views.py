from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .serializers import MemberSerializer
from .models import Service,Member,Payment
from .forms import MemberShipForm
from django.db.models import Q
# Create your views here.
def index(request):
    form=MemberShipForm()
    context={"form":form}
    return render(request,"index.html",context)

def SignupMember(request):
    if request.method == "POST":
        form=MemberShipForm(request.POST)
        form.save()
        return redirect(index)
        
def PackagePrice(request,package_id):
    package=Service.objects.get(pk=package_id)
    return JsonResponse({"price":package.price})

def Search(request,keyword):
    members=Member.objects.filter(Q(name__icontains=keyword)|Q(identity__icontains=keyword)| Q(cnic__icontains=keyword) |Q(phone__icontains=keyword))
    members=MemberSerializer(members,many=True)
    return JsonResponse(members.data,safe=False)

def Ledger(request,member_id):
    member=Member.objects.get(pk=member_id)
    payments= Payment.objects.filter(user=member)
    context={"member":member,"payments":payments}
    return render(request,"ledger.html",context)
