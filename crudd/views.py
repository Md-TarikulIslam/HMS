from typing import Any
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import EmployeeDetails, PatientDetails, DoctorDetails, SalaryDetails, MedicineDetails, OPDDetails, IPDDetails, OTDetails, BEDetails
from django.contrib import messages
from django.core.mail import message, send_mail
from django.conf import settings
from django.db.models import Q


# Index
def index(request):
    return render(request,"crud/index.html")

# Employee
def Viewemployees(request):
    if 'e' in request.GET:
        e=request.GET['e']
        multiple_e = Q(Q(name__icontains=e) | Q(email__icontains=e) | Q(phone__icontains=e) | Q(address__icontains=e) )
        all_data=EmployeeDetails.objects.filter(multiple_e)
    else:
        all_data = EmployeeDetails.objects.all()
    emp = {'all_data':all_data}
    return render(request, 'crud/employee.html', emp)

# Insert Data
def insert_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        image = request.FILES['image_file']
        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = EmployeeDetails(name=name, email=email, phone=phone, address=address,image=image)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewemployees)
  

# Update Data
def update_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        image = request.FILES['image_file']

        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = EmployeeDetails(name=name, email=email, phone=phone, address=address,image=image,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewemployees)


# Delete Data
def delete_data(request,id):
    if request.method == "GET":
        get_data = EmployeeDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewemployees)



# Patient
def Viewpatient(request):
    if 'p' in request.GET:
        p=request.GET['p']
        multiple_p = Q(Q(pname__icontains=p) | Q(pemail__icontains=p) | Q(pphone__icontains=p) | Q(paddress__icontains=p) )
        all=PatientDetails.objects.filter(multiple_p)
    else:
        all = PatientDetails.objects.all()
    emp = {'all':all}
    return render(request, 'crud/patient.html', emp)



# Insert Data
def ins_data(request):
    if request.method == "POST":
        name = request.POST['pname']
        email = request.POST['pemail']
        address = request.POST['paddress']
        phone = request.POST['pphone']
        # image = request.FILES['image_file']
        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = PatientDetails(pname=name, pemail=email, pphone=phone, paddress=address)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewpatient)


# Update Data
def upd_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        # image = request.FILES['image_file']

        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = PatientDetails(pname=name, pemail=email, pphone=phone, paddress=address,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewpatient)


# Delete Data
def del_data(request,id):
    if request.method == "GET":
        get_data = PatientDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewpatient)


# Contact
def viewContact(request):
    return render(request, 'crud/contact.html')

def message_meView(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    subject = request.POST.get('subject')
    query = request.POST.get('query')
    email_body ='First Name: ' +firstname+' , '+'Last Name: '+lastname+' , '+'Subject: '+subject+' , '+'Query: '+query
    sender = settings.EMAIL_HOST_USER
    receivers=['example@gmail.com']

    send_mail(subject, email_body, sender, receivers)
    
    return HttpResponseRedirect('http://127.0.0.1:8000/contact/')


# Doctor
def Viewdoctor(request):
    if 'd' in request.GET:
        d=request.GET['d']
        multiple_d = Q(Q(dname__icontains=d) | Q(demail__icontains=d) | Q(dphone__icontains=d) )
        all_d=DoctorDetails.objects.filter(multiple_d)
    else:
        all_d = DoctorDetails.objects.all()
    emp = {'all_d':all_d}
    return render(request, 'crud/doctor.html', emp)


# Insert Data
def in_data(request):
    if request.method == "POST":
        name = request.POST['dname']
        email = request.POST['demail']
        specialist = request.POST['dspecialist']
        phone = request.POST['dphone']
        if(name==''or email==''or specialist==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = DoctorDetails(dname=name, demail=email, dphone=phone, dspecialist=specialist)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewdoctor)


# Update Data
def up_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        specialist = request.POST['specialist']
        phone = request.POST['phone']

        if(name==''or email==''or specialist==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = DoctorDetails(dname=name, demail=email,dspecialist=specialist, dphone=phone,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewdoctor)


# Delete Data
def de_data(request,id):
    if request.method == "GET":
        get_data = DoctorDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewdoctor)


# Salary
def Viewsalary(request):
    if 'sa' in request.GET:
        sa=request.GET['sa']
        multiple_sa = Q(Q(sname__icontains=sa) | Q(saccountno__icontains=sa) | Q(smonth__icontains=sa) )
        all_s=SalaryDetails.objects.filter(multiple_sa)
    else:
        all_s = SalaryDetails.objects.all()
    emp = {'all_s':all_s}
    return render(request, 'crud/salary.html', emp)

# Insert Data
def n_data(request):
    if request.method == "POST":
        name = request.POST['sname']
        accountno = request.POST['saccountno']
        amount = request.POST['samount']
        month = request.POST['smonth']
        if(name==''or accountno==''or amount==''or month==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = SalaryDetails(sname=name, saccountno=accountno,  samount=amount, smonth=month)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewsalary)


# Update Data
def p_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        accountno = request.POST['accountno']
        amount = request.POST['amount']
        month = request.POST['month']
  

        if(name==''or accountno==''or amount==''or month==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = SalaryDetails(sname=name, saccountno=accountno, samount=amount,smonth=month,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewsalary)


# Delete Data
def e_data(request,id):
    if request.method == "GET":
        get_data = SalaryDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewsalary)


# Medicine
def Viewmedicine(request):
    if 'm' in request.GET:
        m=request.GET['m']
        multiple_m = Q(Q(mname__icontains=m) | Q(mtype__icontains=m) )
        s=MedicineDetails.objects.filter(multiple_m)
    else:
        s = MedicineDetails.objects.all()
    emp = {'s':s}
    return render(request, 'crud/medicine.html', emp)


# Insert Data
def give_data(request):
    if request.method == "POST":
        name = request.POST['mname']
        ty = request.POST['mtype']
        price = request.POST['mprice']
        stock = request.POST['mstock']
    
        if(name==''or ty==''or price==''or stock==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = MedicineDetails(mname=name,mtype=ty, mprice=price, mstock=stock)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewmedicine)


# Update Data
def ed_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        ty = request.POST['ty']
        price = request.POST['price']
        stock = request.POST['stock']


        if(name==''or ty==''or price==''or stock==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = MedicineDetails(mname=name, mtype=ty, mprice=price, mstock=stock, id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewmedicine)


# Delete Data
def erase_data(request,id):
    if request.method == "GET":
        get_data = MedicineDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewmedicine)


# OPD
def Viewopd(request):
    if 'o' in request.GET:
        o=request.GET['o']
        multiple_o = Q(Q(oname__icontains=o) | Q(odate__icontains=o) | Q(ophone__icontains=o) | Q(oaddress__icontains=o) )
        ss=OPDDetails.objects.filter(multiple_o)
    else:
        ss = OPDDetails.objects.all()
    emp = {'ss':ss}
    return render(request, 'crud/opd.html', emp)


# Insert Data
def inser_data(request):
    if request.method == "POST":
        name = request.POST['oname']
        address = request.POST['oaddress']
        phone = request.POST['ophone']
        date = request.POST['odate']
    
        if(name==''or address==''or phone==''or date==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = OPDDetails(oname=name,oaddress=address, ophone=phone, odate=date)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewopd)


# Update Data
def upda_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        date = request.POST['date']


        if(name==''or address==''or phone==''or date==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = OPDDetails(oname=name, oaddress=address, ophone=phone, odate=date, id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewopd)


# Delete Data
def delet_data(request,id):
    if request.method == "GET":
        get_data = OPDDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewopd)

# IPD
def Viewipd(request):
    if 's' in request.GET:
        s=request.GET['s']
        multiple_s = Q(Q(iname__icontains=s) | Q(idate__icontains=s) | Q(iphone__icontains=s) | Q(iaddress__icontains=s) )
        al=IPDDetails.objects.filter(multiple_s)
    else:
        al =IPDDetails.objects.all()
    emp = {'al':al}
    return render(request, 'crud/ipd.html', emp)

# Insert Data
def inse_data(request):
    if request.method == "POST":
        name = request.POST['iname']
        date = request.POST['idate']
        address = request.POST['iaddress']
        phone = request.POST['iphone']
        # image = request.FILES['image_file']
        if(name==''or date==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = IPDDetails(iname=name, idate=date, iphone=phone, iaddress=address)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewipd)

# Update Data
def updat_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        date = request.POST['date']
        address = request.POST['address']
        phone = request.POST['phone']


        if(name==''or date==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = IPDDetails(iname=name, idate=date, iphone=phone, iaddress=address,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewipd)


# Delete Data
def dele_data(request,id):
    if request.method == "GET":
        get_data = IPDDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewipd)


# IPD
def Viewipd(request):
    if 's' in request.GET:
        s=request.GET['s']
        multiple_s = Q(Q(iname__icontains=s) | Q(idate__icontains=s) | Q(iphone__icontains=s) | Q(iaddress__icontains=s) )
        al=IPDDetails.objects.filter(multiple_s)
    else:
        al =IPDDetails.objects.all()
    emp = {'al':al}
    return render(request, 'crud/ipd.html', emp)

# Insert Data
def inse_data(request):
    if request.method == "POST":
        name = request.POST['iname']
        date = request.POST['idate']
        address = request.POST['iaddress']
        phone = request.POST['iphone']
        # image = request.FILES['image_file']
        if(name==''or date==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = IPDDetails(iname=name, idate=date, iphone=phone, iaddress=address)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewipd)

# Update Data
def updat_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        date = request.POST['date']
        address = request.POST['address']
        phone = request.POST['phone']


        if(name==''or date==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = IPDDetails(iname=name, idate=date, iphone=phone, iaddress=address,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewipd)


# Delete Data
def dele_data(request,id):
    if request.method == "GET":
        get_data = IPDDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewipd)


# OT
def Viewot(request):
    if 'ot' in request.GET:
        ot=request.GET['ot']
        multiple_ot = Q(Q(opname__icontains=ot) | Q(odname__icontains=ot) | Q(opphone__icontains=ot) )
        xx=OTDetails.objects.filter(multiple_ot)
    else:
        xx =OTDetails.objects.all()
    emp = {'xx':xx}
    return render(request, 'crud/ot.html', emp)

# Insert Data
def inot(request):
    if request.method == "POST":
        name = request.POST['opname']
        dname = request.POST['odname']
        date = request.POST['opdate']
        cause = request.POST['opcause']
        room = request.POST['oproom']
        phone = request.POST['opphone']
        if(name==''or date==''or dname==''or phone=='' or cause=='' or room==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = OTDetails(opname=name, odname=dname, opdate=date, opphone=phone, opcause=cause, oproom=room)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewot)

# Update Data
def upot(request,id):
    if request.method == "POST":
        name = request.POST['name']
        dname = request.POST['dname']
        date = request.POST['date']
        cause = request.POST['cause']
        room = request.POST['room']
        phone = request.POST['phone']


        if(name==''or date==''or name==''or phone=='' or cause=='' or room==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = OTDetails(opname=name, odname=dname, opdate=date, opphone=phone, oproom=room,opcause=cause,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewot)


# Delete Data
def deot(request,id):
    if request.method == "GET":
        get_data = OTDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewot)



# BED
def Viewbed(request):
    if 'b' in request.GET:
        b=request.GET['b']
        multiple_b = Q(Q(broom__icontains=b) | Q(bfloor__icontains=b)  )
        yy=BEDetails.objects.filter(multiple_b)
    else:
        yy =BEDetails.objects.all()
    emp = {'yy':yy}
    return render(request, 'crud/bed.html', emp)

# Insert Data
def inb(request):
    if request.method == "POST":
        room = request.POST['broom']
        floor = request.POST['bfloor']
        seat = request.POST['bseat']
      
        if(room==''or floor==''or seat==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = BEDetails(broom=room, bfloor=floor, bseat=seat)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(Viewbed)

# Update Data
def upb(request,id):
    if request.method == "POST":
        room = request.POST['room']
        floor = request.POST['floor']
        seat = request.POST['seat']
    


        if(room==''or floor==''or seat==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = BEDetails(broom=room, bfloor=floor, bseat=seat,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(Viewbed)


# Delete Data
def deb(request,id):
    if request.method == "GET":
        get_data = BEDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(Viewbed)


