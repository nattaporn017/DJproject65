# from django.forms import modelformset_factory
#
# import datetime, os
# from django.db.models import Q
# from django.core.paginator import (Paginator, EmptyPage,PageNotAnInteger,)
#
# from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
# from django.contrib import messages
# from .models import *
# from Express.forms import *
# import datetime

# from django.contrib.auth import authenticate, login, logout

import datetime
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from Express.forms import *
import datetime, os
from django.db.models import Q
from django.core.paginator import (Paginator, EmptyPage,PageNotAnInteger,)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    countEmp = Employees.objects.count()
    print("countEmp:" + str(countEmp))
    if countEmp == 0:
        return redirect('empNew')
    else:
        return render(request, 'home.html')
def news(request):
    return render(request,'news.html')

def info(request):
    return render(request,'CRUD/info.html')
def warning(request):
    return render(request, 'warning.html')

def question(request):
    return render(request, 'question.html')

def fast(request):
    return render(request, 'fast.html')

def howto(request):
    return render(request, 'howto.html')

def calculation(request):
    return render(request,'calculation.html')

def userLogout(request):
    del request.session["userId"]
    del request.session["userName"]
    del request.session["userStatus"]
    logout(request)
    return  redirect('home')

def chkPermission(request):
    if 'userStatus' in request.session:
        userStatus = request.session['userStatus']
        if userStatus == 'customer':
            messages.add_message(request, messages.WARNING, "ท่านกำลังเข้าใช้ในส่วนที่ไม่ได้รับอนุญาต!!!")
            return False
        else:
            return True
    else:
        if Employees.objects.count() != 0:
            return False
        else:
            return True
################################################ Emp
def empNew(request):
    if not chkPermission(request):
        return redirect('home')
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            eid = request.POST['eid']
            name = request.POST['name']
            email = 'none@gmail.com'
            password = request.POST['password']
            user = User.objects.create_user(eid, email, password)
            user.first_name = name
            user.is_staff = True
            user.save()
            return redirect('userLogin')
        else:
            context = {'form': form}
            return render(request, 'crudProcess/creatEmp.html', context)
    else:
        form = EmployeesForm()
        context = {'form': form}
        return render(request, 'crudProcess/creatEmp.html', context)

@login_required(login_url='userLogin')
def createEmp(request):
    if not chkPermission(request):
        return redirect('home')
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            eid = request.POST['eid']
            name = request.POST['name']
            email = 'none@gmail.com'
            password = request.POST['password']
            user = User.objects.create_user(eid, email, password)
            user.first_name = name
            user.is_staff = True
            user.save()
            return redirect('listEmp')
        else:
            context = {'form': form}
            return render(request, 'crudProcess/creatEmp.html', context)
    else:
        form = EmployeesForm()
        context = {'form': form}
        return render(request, 'crudProcess/creatEmp.html', context)
@login_required(login_url='userLogin')
def listEmp(request):
    result = Employees.objects.all()
    context ={'employee' : result}
    return render(request, 'crudProcess/listEmp.html', context)
@login_required(login_url='userLogin')
def oneEmp(request,eid):
    emp_info = Employees.objects.get(eid=eid)
    context= {'employee': emp_info}
    return render(request, 'crudProcess/oneEmp.html', context)
@login_required(login_url='userLogin')
def updateEmp(request,eid):
    context = {}
    obj = Employees.objects.get(eid=eid)
    form = EmployeesForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listEmp')
    else:
        context["form"] = form
        return render(request, "crudProcess/updateEmp.html", context)
@login_required(login_url='userLogin')
def gtdelEmp(request,eid):
    Employee_info = Employees.objects.get(eid=eid)
    context= {'employee': Employee_info}
    return render(request, 'crudProcess/deleteEmp.html', context)
@login_required(login_url='userLogin')
def deleteEmp(request, eid):
    Employee_info = Employees.objects.get(eid=eid)
    if request.method == "GET":
        Employee_info.delete()
        return redirect('listEmp')
################################################ Branch
@login_required(login_url='userLogin')
def createBranch(request):
    context = {}
    if request.method == 'POST':
        form = BranchForm(request.POST)
        obj = Branch.objects.filter(branch_id=request.POST['branch_id'])
        if obj:
            context["form"] = form
            return render(request, "crudProcess/createBranch.html", context)
        if form.is_valid():
            form.save()
            return redirect('listBranch')
        else:
            return redirect('listBranch')
    else:
        form = BranchForm()
    context = {
        'form': form
    }
    return render(request, 'crudProcess/creatBranch.html', context)
@login_required(login_url='userLogin')
def listBranch(request):
    result = Branch.objects.all()
    context ={'result' : result}
    return render(request, 'crudProcess/listBranch.html', context)
@login_required(login_url='userLogin')
def oneBranch(request,branch_id):
    branch_info = Branch.objects.get(branch_id=branch_id)
    context= {'branch': branch_info}
    return render(request, 'crudProcess/oneBranch.html', context)
@login_required(login_url='userLogin')
def updatebranch(request,branch_id):
    context = {}
    obj = Branch.objects.get(branch_id=branch_id)
    form = BranchForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listBranch')
    else:
        context["form"] = form
        return render(request, "crudProcess/updateBranch.html", context)
@login_required(login_url='userLogin')
def gtdelBranch(request,branch_id):
    branch_info = Branch.objects.get(branch_id=branch_id)
    context= {'branch': branch_info}
    return render(request, 'crudProcess/deleteBranch.html', context)
@login_required(login_url='userLogin')
def deleteBranch(request, branch_id):
    branch_info = Branch.objects.get(branch_id=branch_id)
    if request.method == "GET":
        branch_info.delete()
        return redirect('listBranch')


######################################################### Categories
@login_required(login_url='userLogin')
def createCategories(request):
    context = {}
    if request.method == 'POST':
        form = CategoiesForm(request.POST)
        obj = Categories.objects.filter(cgid=request.POST['cgid'])
        if obj:
            context["form"] = form
            return render(request, "crudProcess/creatCategories.html", context)
        if form.is_valid():
            form.save()
            return redirect('listCategories')
        else:
            return redirect('listCategories')
    else:
        form = CategoiesForm()
    context = {
        'form': form
    }
    return render(request, 'crudProcess/creatCategories.html', context)
@login_required(login_url='userLogin')
def listCategories(request):
    result = Categories.objects.all()
    context ={'result' : result}
    return render(request, 'crudProcess/listCategories.html', context)
@login_required(login_url='userLogin')
def oneCategories(request,cgid):
    categories_info = Categories.objects.get(cgid=cgid)
    context= {'categories': categories_info}
    return render(request, 'crudProcess/oneCategories.html', context)
@login_required(login_url='userLogin')
def updateCategories(request,cgid):
    context = {}
    obj = Categories.objects.get(cgid=cgid)
    form = CategoiesForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listCategories')
    else:
        context["form"] = form
        return render(request, "crudProcess/updateCategories.html", context)
@login_required(login_url='userLogin')
def gtdelCategories(request,cgid):
    categories_info = Categories.objects.get(cgid=cgid)
    context= {'categories': categories_info}
    return render(request, 'crudProcess/deleteCategories.html', context)
@login_required(login_url='userLogin')
def deleteCategories(request, cgid):
    categories_info = Categories.objects.get(cgid=cgid)
    if request.method == "GET":
        categories_info.delete()
        return redirect('listCategories')


######################################################### Acc
@login_required(login_url='userLogin')
def createAcc(request):
    context = {}
    if request.method == 'POST':
        form = AccessoriessForm(request.POST)
        obj = Accessoriess.objects.filter(aid=request.POST['aid'])
        if obj:
            context["form"] = form
            return render(request, "crudProcess/creatAcc.html", context)
        if form.is_valid():
            form.save()
            return redirect('listAcc')
        else:
            return redirect('listAcc')
    else:
        form = AccessoriessForm()
    context = {
        'form': form
    }
    return render(request, 'crudProcess/creatAcc.html', context)
@login_required(login_url='userLogin')
def listAcc(request):
    result = Accessoriess.objects.all()
    context ={'result' : result}
    return render(request, 'crudProcess/listAccessories.html', context)
@login_required(login_url='userLogin')
def oneAcc(request,aid):
    acc_info = Accessoriess.objects.get(aid=aid)
    context= {'acc': acc_info}
    return render(request, 'crudProcess/oneAccessories.html', context)
@login_required(login_url='userLogin')
def updateAcc(request,aid):
    context = {}
    obj = Accessoriess.objects.get(aid=aid)
    form = AccessoriessForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listAcc')
    else:
        context["form"] = form
        return render(request, "crudProcess/updateAcc.html", context)
@login_required(login_url='userLogin')
def gtdelAcc(request,aid):
    acc_info = Accessoriess.objects.get(aid=aid)
    context= {'acc': acc_info}
    return render(request, 'crudProcess/deleteAcc.html', context)
@login_required(login_url='userLogin')
def deleteAcc(request, aid):
    acc_info = Accessoriess.objects.get(aid=aid)
    if request.method == "GET":
        acc_info.delete()
        return redirect('listAcc')
#########################################################customer
@login_required(login_url='userLogin')
def createCus(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            conf_password = request.POST['conf_password']
            if password == conf_password:
                form.save()

                cid = request.POST['cid']
                name = request.POST['name']
                email = 'none@gmail.com'
                password = request.POST['password']
                user = User.objects.create_user(cid, email, password)
                user.first_name = name
                user.is_staff = False
                user.save()

                return redirect('listCus')
            else:
                messages.add_message(request, messages.WARNING, "รหัสผ่านกับรหัสผ่านที่ยืนยันไม่ตรงกัน...")
                context = {'form': form}
                return render(request, 'crudProcess/createCus.html', context)
        else:
            messages.add_message(request, messages.WARNING, "ป้อนข้อมูลไม่ถูกต้อง ไม่สมบูรณ์...")
            context = {'form': form}
            return render(request, 'crudProcess/createCus.html', context)
    else:
        form = CustomersForm()
        context = {'form': form}
        return render(request, 'crudProcess/createCus.html', context)
@login_required(login_url='userLogin')
def oneCus(request,cid):
    customer_info = Customers.objects.get(cid=cid)
    context= {'customers': customer_info}
    return render(request, 'crudProcess/oneCus.html', context)
@login_required(login_url='userLogin')
def listCus(request):
    if not chkPermission(request):
        return redirect('home')
    customers = Customers.objects.all().order_by('cid')
    context = {'customers':customers}
    return render(request, 'crudProcess/listCus.html', context)
@login_required(login_url='userLogin')
def updateCus(request,cid):
    context = {}
    obj = Customers.objects.get(cid=cid)
    form = CustomersForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listCus')
    else:
        context["form"] = form
        return render(request, "crudProcess/updateCus.html", context)
@login_required(login_url='userLogin')
def gtdelCus(request,cid):
    customers_info = Customers.objects.get(cid=cid)
    context= {'customers': customers_info}
    return render(request, 'crudProcess/deleteCus.html', context)
@login_required(login_url='userLogin')
def deleteCus(request, cid):
    customers_info = Customers.objects.get(cid=cid)
    if request.method == "GET":
        customers_info.delete()
        return redirect('listCus')

######################################################### ลงทะเบียน
def cusRegister(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            conf_password = request.POST['conf_password']
            if password == conf_password:
                form.save()

                cid = request.POST['cid']
                name = request.POST['name']
                email = 'none@gmail.com'
                password = request.POST['password']
                user = User.objects.create_user(cid, email, password)
                user.first_name = name
                user.is_staff = False
                user.save()

                return redirect('userLogin')
            else:
                messages.add_message(request, messages.WARNING, "รหัสผ่านกับรหัสผ่านที่ยืนยันไม่ตรงกัน...")
                context = {'form': form}
                return render(request, 'crudProcess/cusRegister.html', context)
        else:
            messages.add_message(request, messages.WARNING, "ป้อนข้อมูลไม่ถูกต้อง ไม่สมบูรณ์...")
            context = {'form': form}
            return render(request, 'crudProcess/cusRegister.html', context)
    else:
        form = CustomersForm()
        context = {'form': form}
        return render(request, 'crudProcess/cusRegister.html', context)

def userLogin(request):
    if request.method == 'POST':
        userName = request.POST.get("userName")
        userPass = request.POST.get("userPass")

        user = authenticate(username=userName, password=userPass)
        if user is not None:
            login(request, user)
            if user.is_staff == 0:
                user = Customers.objects.get(cid=userName)
                request.session['userId'] = user.cid
                request.session['userName'] = user.name
                request.session['userStatus'] = 'customer'
            else:
                emp = Employees.objects.get(eid=userName)
                request.session['userId'] = emp.eid
                request.session['userName'] = emp.name
                request.session['userStatus'] = emp.position
            messages.add_message(request, messages.INFO, "Login success..")
            if request.session.get('orderActive'):
                del request.session['orderActive']
                return redirect('checkout')
            else:
                return redirect('home')
        else:
            messages.error(request, "User Name or Password not correct..!!!")
            data = {'userName': userName}
            return render(request, 'userLogin.html', data)
    else:
         data = {'userName': ''}
         return render(request, 'userLogin.html', data)
@login_required(login_url='userLogin')
def cusUpdate(request, cid):
    customer = get_object_or_404(Customers, cid=cid)
    if request.method == 'POST':
        form = CustomersForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            if request.session.get('userStatus') == 'customer':
                return redirect('home')
            else:
                return redirect('cusList')
        else:
            context = {'form': form}
            return render(request, 'crudProcess/cusUpdate.html', context)
    else:
        form = CustomersForm(instance=customer)
        form.updateForm()
        context = {'form': form}
        return render(request, 'crudProcess/cusUpdate.html', context)

@login_required(login_url='userLogin')
def cusChangePassword(request):
    userId = request.session.get('userId')
    user = None
    if request.method == 'POST':
        form=ChangePasswordForm(request.POST or None)

        context = {'form': form}
        old = authenticate(username=userId, password=request.POST['oldPassword'])
        if old:
            if request.POST['newPassword'] == request.POST['confirmPassword']:
                old.set_password(request.POST['newPassword'])
                old.save()
                messages.add_message(request, messages.INFO, "เปลี่ยนรหัสผ่านเสร็จเรียบร้อย...")
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, "รหัสผ่านใหม่กับรหัสที่ยืนยันไม่ตรงกัน...")
                return render(request, 'crudProcess/cusChangePassword.html', context)
        else:
            messages.add_message(request, messages.ERROR, "รหัสผ่านเดิมที่ระบุไม่ถูกต้อง...")
            return render(request, 'crudProcess/cusChangePassword.html', context)
    else:
        form=ChangePasswordForm(initial={'userId':userId})
        context ={'form':form}
        return render(request, 'crudProcess/cusChangePassword.html', context)


###สินค้า
def shopping(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        qnt = int(request.POST.get('qnt'))
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(aid)
            if quantity:
                cart[aid] = quantity + qnt
            else:
                cart[aid] = qnt
        else:
            cart = {}
            cart[aid] = qnt
        request.session['cart'] = cart
        request.session['count'] = len(cart)
        return redirect('shopping')
    else:
        accessoriess = Accessoriess.objects.all().order_by('aid')
        data = {'accessoriess':accessoriess}
        return render(request, 'shopping.html', data)

def showBasket(request):
    cart = request.session.get('cart')
    if request.method == 'POST':
        action = request.POST.get('action')
        aid = request.POST.get('aid')
        qnt = int(request.POST.get('qnt'))
        if action=="Update":
            if cart[aid]:
                cart[aid] = qnt
        else:
            del cart[aid]
        request.session['cart'] = cart
        request.session['count'] = len(cart)
    if len(cart) == 0:
        del request.session['cart']
        del request.session['count']
        del request.session['sum']
        return redirect('shopping')
    cart = request.session.get('cart')
    items = []
    sum=0.00
    for item in cart:
        accessories = Accessoriess.objects.get(aid=item)
        total= accessories.price * cart[item]
        sum+=total
        items.append({'accessories':accessories, 'quantity':cart[item], 'total':total})
    request.session['sum'] = sum
    data={'items':items}
    return render(request, 'showBasket.html',data)
@login_required(login_url='userLogin')
def clearBasket(request):
    del request.session['cart']
    del request.session['count']
    del request.session['sum']
    return redirect('shopping')
@login_required(login_url='userLogin')
def checkout(request):
    cart = request.session.get('cart')
    items = []
    sum = 0.00
    if cart:
        if not request.session.get('userId'):
            request.session['orderActive'] = True
            return redirect('userLogin')
        cart = request.session.get('cart')
        date = datetime.datetime.now()
        customer = get_object_or_404(Customers, cid=request.session.get('userId'))
        order = Orders()
        order.odate = date.strftime('%Y-%m-%d %H:%M:%S')
        order.customer = customer
        for item in cart:
            accessoriess = Accessoriess.objects.get(aid=item)
            total=accessoriess.price * cart[item]
            sum+=total
            items.append({'accessories':accessoriess, 'quantity':cart[item], 'total':total})
        request.session['sum'] = sum
        data={'items':items, 'order':order}
        return render(request, 'checkout.html', data)
    else:
        messages.add_message(request, messages.WARNING, "ไม่มีสินค้าในรถเข็นสินค้า!!!..")
        return redirect('shopping')
#ออเดอร์
@login_required(login_url='userLogin')
def order(request):
    cart = request.session.get('cart')
    if cart is None:
        return redirect('shopping')
    items = []
    date = datetime.datetime.now()
    customer = get_object_or_404(Customers, cid=request.session.get('userId'))
    order = Orders()
    order.newOrderId()
    order.odate = date.strftime('%Y-%m-%d %H:%M:%S')
    order.customer = customer
    order.status = "1"
    order.save()
    for item in cart:
        accessoriess = Accessoriess.objects.get(aid=item)
        quantity = cart[item]
        total = accessoriess.price * cart[item]
        orderDetail = OrderDetails()
        orderDetail.order_id = order.oid
        orderDetail.accessories_id=accessoriess.aid
        orderDetail.oprice=accessoriess.price
        orderDetail.quantity = quantity
        orderDetail.save()
        items.append({'accessories': accessoriess, 'quantity': cart[item], 'total': total})
    count = request.session.get('count')
    sum = request.session.get('sum')
    data = {'items': items, 'order': order, 'count':count, 'sum':sum}
    del request.session['cart']
    del request.session['count']
    del request.session['sum']
    return render(request, 'summary.html', data)
def showAllOrder(request):
    orders = []
    if request.session.get("userStatus")=='customer':
        customer = get_object_or_404(Customers, cid=request.session.get('userId'))
        orders = None
        if customer:
            orders = Orders.objects.filter(customer=customer).order_by('odate').reverse()
        context = {'customer':customer, 'orders':orders}
        return render(request, 'order/allOrder.html', context)
    else:
        orders = Orders.objects.filter(~Q(status='5')).exclude(status='6').exclude(status='7').order_by('odate').reverse() #อ่านใบสั่งซื้อที่ status 1-4
        context = {'orders': orders}
        return render(request, 'order/allOrder.html', context)
def showOrderDetail(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    if request.method == 'POST':
        return redirect('home')
    else:
        context = {'order': order}
        return render(request, 'order/showOrderDetail.html', context)
@login_required(login_url='userLogin')
def orderCancel(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    form = CancelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            order.status = '6'
            order.save()
        return redirect('allOrder')
    else:
        form = CancelForm(initial={'order': order})
        context = {'form': form, 'order': order}
        return render(request, 'order/orderCancel.html', context)
@login_required(login_url='userLogin')
def transfers(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    form = TranfersForm(request.POST or None, files=request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            order.status='3'
            order.save()
        return redirect('allOrder')
    else:
        form = TranfersForm(initial={'order':order})
        context = {'form':form, 'order':order }
        return render(request, 'order/moneyTransfer.html', context)
@login_required(login_url='userLogin')
def accept(request,oid):
    order = get_object_or_404(Orders, oid=oid)
    employee = get_object_or_404(Employees, eid=request.session.get('userId'))
    accept = Accepts()
    accept.order = order
    accept.employee = employee
    accept.save()
    order.status = '4'
    order.save()
    return redirect('allOrder')
@login_required(login_url='userLogin')
def orderConfirm(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    employee = get_object_or_404(Employees, eid=request.session.get('userId'))
    confirm = Confirms()
    confirm.order = order
    confirm.employee = employee
    confirm.save()
    order.status = '2'
    order.save()
    return redirect('allOrder')
@login_required(login_url='userLogin')
def orderReject(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    employee = get_object_or_404(Employees, eid=request.session.get("userId"))
    form = RejectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            order.status = '7'
            order.save()
        return redirect('allOrder')
    else:
        form = RejectForm(initial={'order': order, 'employee': employee})
        context = {'form': form, 'order': order}
        return render(request, 'orderReject.html', context)
@login_required(login_url='userLogin')
def productSend(request, oid):
    order = get_object_or_404(Orders, oid=oid)
    employee = get_object_or_404(Employees, eid=request.session.get("userId"))
    form = SendForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            order.status = '5'
            order.save()
        return redirect('allOrder')
    else:
        form = SendForm(initial={'order': order, 'employee':employee})
        context = {'form': form, 'order': order}
        return render(request, 'order/productSend.html', context)

# import plotly.graph_objs as go
# import pandas as pd
# import plotly.express as px
#
# def dashboardBarGraph(request):
#     All = Accessoriess.objects.all()
#     products = []
#     amounts = []
#     for item in All:
#         products.append(item.name)
#         amounts.append(item.getSaleAmount())
#     # กรณีอ่านค่าจากบางฟิลด์ใน model มาใช้งาน
#     # products = Products.objects.values_list('name', 'samplesale__amount')
#     # df = pd.DataFrame(products,  columns=['Product', 'Amount'])
#     df = pd.DataFrame({"Product":products, "Amount":amounts}, columns=['Product', 'Amount'])
#     fig = px.bar(df, x='Product', y='Amount', title="แผนภูมิแท่งแสดงยอดขายแยกตามรายชื่อสินค้า")
#     fig.update_layout(autosize = False, width = 600,  height = 400,
#                       margin = dict(l=10, r=10, b=100, t=100, pad=5 ),
#                       paper_bgcolor = "aliceblue",)
#     chart = fig.to_html()
#     context = {'chart':chart}
#     return render(request, "dashboard.html", context)


# @login_required(login_url='userLogin')
# def service(request):
#     context = {}
#
#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         obj = Servise.objects.filter(weight=request.POST['weight'])
#         date = datetime.datetime.now()
#         if obj:
#             context["form"] = form
#             return render(request, 'order/service.html', context)
#         if form.is_valid():
#             service = Servise()
#             service.newId()
#             service.sdate = date.strftime('%Y-%m-%d %H:%M:%S')
#             service.status="1"
#             service.save()
#         return redirect('home')
#     else:
#         form = ServiceForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'order/service.html', context)


# def service(request):
#     context = {}
#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         obj = Servise.objects.filter(sid=request.POST['sid'])
#         if obj:
#
#             context["form"] = form
#             return render(request, "order/service.html", context)
#         if form.is_valid():
#             form = Servise()
#             form.newId()
#             form.status ='1'
#             form.save()
#             return redirect('home')
#         else:
#             return redirect('home')
#     else:
#         form = ServiceForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'order/service.html', context)

# @login_required(login_url='userLogin')
# def service(request):
#     if not chkPermission(request):
#         return redirect('home')
#     if request.method == 'POST':
#         form = Servise()
#         form.newId()
#         form.sdate = datetime.datetime.now()
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#
#             form.save()
#             return redirect('home')
#         else:
#             context = {'form': form}
#             return render(request, 'order/service.html', context)
#     else:
#         form = ServiceForm()
#         context = {'form': form}
#         return render(request, 'order/service.html', context)



#noey
