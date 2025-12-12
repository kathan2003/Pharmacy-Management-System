from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Dealer, Employee, Customer, Medicine, Purchase


def home(request):
    return render(request, 'pharma/index.html')


# ---- Dealer Views ----
def dealerform(request):
    return render(request, 'pharma/dealer.html', {'add': True})


def dealerforminsert(request):
    if request.method == 'POST':
        try:
            dealer = Dealer()
            dealer.dname = request.POST['dname']
            dealer.address = request.POST['address']
            dealer.phn_no = request.POST['pno']
            dealer.email = request.POST['email']
            dealer.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return redirect('dealerform')


def dealerformupdate(request, foo):
    dealer = get_object_or_404(Dealer, pk=foo)
    if request.method == 'POST':
        try:
            dealer.dname = request.POST['dname']
            dealer.address = request.POST['address']
            dealer.phn_no = request.POST['pno']
            dealer.email = request.POST['email']
            dealer.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return render(request, 'pharma/dealer.html', {'dealer': dealer})


def dealerformview(request, foo):
    dealer = get_object_or_404(Dealer, pk=foo)
    return render(request, 'pharma/dealer.html', {'dealer': dealer})


def dealerformdelete(request, foo):
    dealer = get_object_or_404(Dealer, pk=foo)
    dealer.delete()
    return redirect('home')


def dealertable(request):
    dealers = Dealer.objects.all()
    return render(request, 'pharma/dealertable.html', {'dealer': dealers})


# ---- Employee Views ----
def empform(request):
    return render(request, 'pharma/emp.html', {'add': True})


def empforminsert(request):
    if request.method == 'POST':
        try:
            emp = Employee()
            emp.e_id = request.POST['eid']
            emp.fname = request.POST['fname']
            emp.lname = request.POST['lname']
            emp.address = request.POST['address']
            emp.phn_no = request.POST['pno']
            emp.email = request.POST['email']
            emp.sal = request.POST['sal']
            emp.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return redirect('empform')


def empformupdate(request, foo):
    emp = get_object_or_404(Employee, pk=foo)
    if request.method == 'POST':
        try:
            emp.e_id = request.POST['eid']
            emp.fname = request.POST['fname']
            emp.lname = request.POST['lname']
            emp.address = request.POST['address']
            emp.phn_no = request.POST['pno']
            emp.email = request.POST['email']
            emp.sal = request.POST['sal']
            emp.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return render(request, 'pharma/emp.html', {'emp': emp})


def empformview(request, foo):
    emp = get_object_or_404(Employee, pk=foo)
    return render(request, 'pharma/emp.html', {'emp': emp})


def empformdelete(request, foo):
    emp = get_object_or_404(Employee, pk=foo)
    emp.delete()
    return redirect('home')


def emptable(request):
    emps = Employee.objects.all()
    return render(request, 'pharma/emptable.html', {'emp': emps})


# ---- Customer Views ----
def custform(request):
    return render(request, 'pharma/cust.html', {'add': True})


def custforminsert(request):
    if request.method == 'POST':
        try:
            cust = Customer()
            cust.fname = request.POST['fname']
            cust.lname = request.POST['lname']
            cust.address = request.POST['address']
            cust.phn_no = request.POST['pno']
            cust.email = request.POST['email']
            cust.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return redirect('custform')


def custformupdate(request, foo):
    cust = get_object_or_404(Customer, pk=foo)
    if request.method == 'POST':
        try:
            cust.fname = request.POST['fname']
            cust.lname = request.POST['lname']
            cust.address = request.POST['address']
            cust.phn_no = request.POST['pno']
            cust.email = request.POST['email']
            cust.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return render(request, 'pharma/cust.html', {'cust': cust})


def custformview(request, foo):
    cust = get_object_or_404(Customer, pk=foo)
    return render(request, 'pharma/cust.html', {'cust': cust})


def custformdelete(request, foo):
    cust = get_object_or_404(Customer, pk=foo)
    cust.delete()
    return redirect('home')


def custtable(request):
    custs = Customer.objects.all()
    return render(request, 'pharma/custtable.html', {'cust': custs})


# ---- Medicine Views ----
def medform(request):
    return render(request, 'pharma/med.html', {'add': True})


def medforminsert(request):
    if request.method == 'POST':
        try:
            med = Medicine()
            med.m_id = request.POST['mid']
            med.mname = request.POST['mname']
            med.dname = request.POST['dname']
            med.desc = request.POST['desc']
            med.price = request.POST['price']
            med.stock = request.POST['stock']
            med.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return redirect('medform')


def medformupdate(request, foo):
    med = get_object_or_404(Medicine, pk=foo)
    if request.method == 'POST':
        try:
            med.m_id = request.POST['mid']
            med.mname = request.POST['mname']
            med.dname = request.POST['dname']
            med.desc = request.POST['desc']
            med.price = request.POST['price']
            med.stock = request.POST['stock']
            med.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return render(request, 'pharma/med.html', {'med': med})


def medformview(request, foo):
    med = get_object_or_404(Medicine, pk=foo)
    return render(request, 'pharma/med.html', {'med': med})


def medformdelete(request, foo):
    med = get_object_or_404(Medicine, pk=foo)
    med.delete()
    return redirect('home')


def medtable(request):
    meds = Medicine.objects.all()
    return render(request, 'pharma/medtable.html', {'med': meds})


# ---- Purchase Views ----
def purchaseform(request):
    return render(request, 'pharma/purchase.html', {'add': True})


def purchaseforminsert(request):
    if request.method == 'POST':
        try:
            purchase = Purchase()
            purchase.pname = request.POST['pname']
            purchase.fname = request.POST['fname']
            purchase.lname = request.POST['lname']
            purchase.qty = request.POST['qty']
            purchase.phn_no = request.POST['pno']
            purchase.price = request.POST['price']
            purchase.total = int(purchase.price) * int(purchase.qty)
            purchase.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return redirect('purchaseform')


def purchaseformupdate(request, foo):
    purchase = get_object_or_404(Purchase, pk=foo)
    if request.method == 'POST':
        try:
            purchase.pname = request.POST['pname']
            purchase.fname = request.POST['fname']
            purchase.lname = request.POST['lname']
            purchase.qty = request.POST['qty']
            purchase.phn_no = request.POST['pno']
            purchase.price = request.POST['price']
            purchase.total = int(purchase.price) * int(purchase.qty)
            purchase.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'pharma/new.html')
    else:
        return render(request, 'pharma/purchase.html', {'purchase': purchase})


def purchaseformview(request, foo):
    purchase = get_object_or_404(Purchase, pk=foo)
    return render(request, 'pharma/purchase.html', {'purchase': purchase})


def purchaseformdelete(request, foo):
    purchase = get_object_or_404(Purchase, pk=foo)
    purchase.delete()
    return redirect('home')


def purchasetable(request):
    purchases = Purchase.objects.all()
    return render(request, 'pharma/purchasetable.html', {'purchase': purchases})


# ---- Auth Views ----
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'pharma/auth.html', {'login_error': 'Invalid username or password', 'active_tab': 'login'})
    return render(request, 'pharma/auth.html', {'active_tab': 'login'})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'pharma/auth.html', {'register_error': "Passwords do not match", 'active_tab': 'register'})

        if User.objects.filter(username=username).exists():
            return render(request, 'pharma/auth.html', {'register_error': "Username already exists", 'active_tab': 'register'})

        User.objects.create_user(username=username, email=email, password=password1)
        return redirect('login')

    return render(request, 'pharma/auth.html', {'active_tab': 'register'})
