import datetime
import random
from django.db import models
from django.utils import timezone
from django.db.models import F, Sum, Count
# # Create your models here.

class Branch(models.Model):
    branch_id = models.CharField(max_length=10,primary_key=True,default="")
    name = models.CharField(max_length=100,default="")
    location = models.CharField(max_length=200, default="")
    tel = models.CharField(max_length=10, default="")
    def __str__(self):
        return  self.branch_id+":"+self.name
class District(models.Model):
    postcode = models.CharField(max_length=5, primary_key=True, default="")
    name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.postcode + ":" + self.name
class Customers(models.Model):
    name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=13, default="")
    birthdate = models.DateField(default=None)
    address = models.TextField(max_length=400, default="")
    tel = models.CharField(max_length=10, default="")
    cid = models.CharField(max_length=20, primary_key=True, default="")

    def __str__(self):
        return self.cid + " : " + self.name
class Employees(models.Model):
    name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=13, default="")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    position = models.CharField(max_length=50, default="")
    birthdate = models.DateField(default=None)
    address = models.TextField(max_length=400, default="")
    tel = models.CharField(max_length=50, default="")
    eid = models.CharField(max_length=20, primary_key=True, default="")

    def __str__(self):
        return self.eid + " : " + self.name + " / " + self.position
    def getCountConfirm(self): #ยืนยัน Order
        count = Confirms.objects.filter(employee=self).aggregate(count=Count('id'))
        return count['count']
    def getCountAccept(self): #ยืนยันการโอนเงิน
        count = Accepts.objects.filter(employee=self).aggregate(count=Count('id'))
        return count['count']
    def getCountSend(self): #การส่งสินค้า
        count = Send.objects.filter(employee=self).aggregate(count=Count('id'))
        return count['count']
class Categories(models.Model):
    cgid = models.CharField(max_length=6, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")
    def __str__(self):
        return str(self.cgid) + ":" + self.name
    def getCountAccessoriess(self):
        count = Accessoriess.objects.filter(category=self).aggregate(count=Count('sid'))
        return count['count']
    def getCountAccessoriess(self):
        categories = Categories.objects.annotate(number_of_accessories=Count('accessories'))

class Servise(models.Model):
    sid = models.CharField(max_length=15, primary_key=True, default="")
    sdate = models.DateTimeField(auto_now_add=True)
    cus = models.ForeignKey(Customers, on_delete=models.CASCADE, default=None)
    person = models.TextField(max_length=800, default="")
    s_start = models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    s_end = models.ForeignKey(District, on_delete=models.CASCADE, default=None)
    type = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    weight = models.FloatField(default=0.00)
    status = models.CharField(max_length=1, default="")
    def __str__(self):
        return self.sid + " : " + self.cus

    def newId(self):
        #OD-yymm-xxxxx  ===> OD-2302-00001
        yy = str(datetime.date.today().strftime('%y'))
        mm = str(datetime.date.today().strftime('%m'))
        hh = str(datetime.date.today().strftime('%H'))
        ii = str(datetime.date.today().strftime('%m'))
        ss = str(datetime.date.today().strftime('%S'))
        # lastSv = Servise.objects.last()
        # date: "Y-m-d H:i:s"
        # if lastSv:
        #     lastId = int(lastSv.sid[9:])
        # else:
        #     lastId = 0
        # id = str(lastId+1)
        # id=id.zfill(5)
        newId  = "SER-"+ yy + mm +hh +ii +ss
        self.sid = newId

    def getStatus(self):
        if self.status == '1':
            return 'รอยืนยันการชำระเงิน'
        elif self.status == '2':
            return 'อยู่ในขั้นตอนการจัดส่ง'
        elif self.status == '3':
            return 'เสร็จสมบูรณ์'

    # def getPrice(self):
    #     if self.s_start == "B40000":
    #         if self.s_end == "ภูผาม่าน" or self.s_end == "สีมพู":
    #             if self.weight <= 1.00:
    #                 price = 150
    #             elif self.weight <= 2.00:
    #                 price = 160
    #             elif self.weight <= 3.00:
    #                 price = 170
    #             elif self.weight <= 4.00:
    #                 price = 180
    #             elif self.weight <= 5.00:
    #                 price = 190
    #             else:
    #                 price = 110
    #         else:
    #             if self.weight <= 1.00:
    #                 price = 45
    #             elif self.weight <= 2.00:
    #                 price = 55
    #             elif self.weight <= 3.00:
    #                 price = 65
    #             elif self.weight <= 4.00:
    #                 price = 75
    #             elif self.weight <= 5.00:
    #                 price = 85
    #             else:
    #                 price = 95
    #     else:
    #         if self.weight <= 1.00:
    #             price = 59
    #         elif self.weight <= 2.00:
    #             price = 69
    #         elif self.weight <= 3.00:
    #             price = 79
    #         elif self.weight <= 4.00:
    #             price = 89
    #         elif self.weight <= 5.00:
    #             price = 99
    #         else:
    #             price = 199
    #         return price['price']









class Accessoriess(models.Model):
    aid = models.CharField(max_length=6, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    price=models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.aid + " : " + self.name

    def __str__(self):
        return self.aid + " : " + self.name + " / " + str(self.price)

    def getCountOrder(self):
        count = OrderDetails.objects.filter(accessories=self).aggregate(count=Count('id'))
        return count['count']

    def getSaleAmount(self):
        amount = Samplesale.objects.filter(accessories=self).aggregate(amount=Sum(F('amount')))
        return amount['amount']
    def getStatus(self):
        if self.status == '1':
            return 'รอยืนยันคำสั่งซื้อ'
        elif self.status == '2':
            return 'รอการโอนเงิน'
        elif self.status == '3':
            return 'รอยืนยันการชำระเงิน'
        elif self.status == '4':
            return 'รอส่งสินค้า'
        elif self.status == '5':
            return 'เสร็จสมบูรณ์'
        elif self.status == '6':
            return 'ยกเลิกคำสั่งซื้อ'
        elif self.status == '7':
            return 'ปฏิเสธคำสั่งซื้อ'
    def getTotal(self):
        total=OrderDetails.objects.filter(order=self).aggregate(total=Sum(F('oprice') * F('quantity')))
        return total['total']



class Orders(models.Model):
    oid = models.CharField(max_length=15, primary_key=True, default="")
    odate = models.DateTimeField(auto_now_add = True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=1, default="")
    def __str__(self):
        return self.oid + " / " + str(self.odate.strftime("%Y-%m-%d")) + " : " + self.customer.name

    def newOrderId(self):
        #OD-yymm-xxxxx  ===> OD-2302-00001
        yy = str(datetime.date.today().strftime('%y'))
        mm = str(datetime.date.today().strftime('%m'))
        lastOrder = Orders.objects.last()
        if lastOrder:
            lastId = int(lastOrder.oid[9:])
        else:
            lastId = 0
        id = str(lastId+1)
        id=id.zfill(5)
        newId  = "OD-"+ yy + mm + "-" + id
        self.oid = newId

    def getStatus(self):
        if self.status == '1':
            return 'รอยืนยันคำสั่งซื้อ'
        elif self.status == '2':
            return 'รอการโอนเงิน'
        elif self.status == '3':
            return 'รอยืนยันการชำระเงิน'
        elif self.status == '4':
            return 'รอส่งสินค้า'
        elif self.status == '5':
            return 'เสร็จสมบูรณ์'
        elif self.status == '6':
            return 'ยกเลิกคำสั่งซื้อ'
        elif self.status == '7':
            return 'ปฏิเสธคำสั่งซื้อ'

    def getOrderDetails(self):
        orderDetails = OrderDetails.objects.filter(order=self)
        return orderDetails

    def getTotal(self):
        total=OrderDetails.objects.filter(order=self).aggregate(total=Sum(F('oprice') * F('quantity')))
        return total['total']

    def getCount(self):
        count= OrderDetails.objects.filter(order=self).aggregate(count=Count('id'))
        return count['count']

class OrderDetails(models.Model):
    order=models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    accessories =models.ForeignKey(Accessoriess, on_delete=models.CASCADE, default=None)
    oprice = models.FloatField(default=0.00)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.order.oid + " : " + self.product.pid + " " + self.product.name + " : " + str(self.quantity)
    def getTotal(self):
        return self.oprice * self.quantity

class Confirms(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
    cdate = models.DateTimeField(auto_now_add = True)
    comment = models.CharField(max_length=200, default="")

class Transfers(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    tdate = models.DateTimeField(auto_now_add = True)
    reference = models.CharField(max_length=35, default="")
    bank = models.CharField(max_length=50, default="")
    bill = models.ImageField(upload_to ='static/bills/', default="")

class Accepts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
    adate =models.DateTimeField(auto_now_add = True)

class Send(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
    sdate = models.DateTimeField(auto_now_add = True)
    barnch = models.ForeignKey(Branch, on_delete=models.CASCADE, default=None)
    tag = models.CharField(max_length=50, default="")

class Cancel(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    cdate = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, default="")

class Reject(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
    rdate = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, default="")

class Samplesale(models.Model): # ตารางสมมุติ เอาไว้เก็บยอดขาย เพื่อเอาไปทำ Dashboard
    accessories = models.ForeignKey(Accessoriess, on_delete=models.CASCADE, default=None)
    datesale = models.DateField(default=None)
    amount = models.IntegerField(default=0)  #ยอดขาย

    def __str__(self):
        return "Hey: " + str(self.id) + " : " + self.accessories.name + " / " + str(self.datesale.year) + " / " + str(self.amount)


#
# #ลูกค้า
# class Customers(models.Model):
#     cid = models.CharField(max_length=20, primary_key=True, default="")
#     name = models.CharField(max_length=50, default="")
#     # birthdate = models.DateField(default=None)
#     address = models.TextField(max_length=400, default="")
#     tel = models.CharField(max_length=10, default="")
#     password = models.CharField(max_length=8, default="")
#     def __str__(self):
#         return self.cid + " : " + self.name
# #################################################################
# #แผนก & พนักงาน & สาขา
# class Departments(models.Model):
#     did = models.CharField(max_length=6, primary_key=True, default="")
#     department = models.CharField(max_length=50, default="")
#     desc = models.CharField(max_length=200, default="")
#     def __str__(self):
#         return self.did + " : " + self.department
# class Employees(models.Model):
#     eid = models.CharField(max_length=20, primary_key=True, default="")
#     name = models.CharField(max_length=50, default="")
#     birthdate = models.DateField(default=None)
#     department = models.ForeignKey(Departments, on_delete=models.CASCADE, default=None)
#     # tel = models.CharField(max_length=10, default="")
#     password = models.CharField(max_length=8, default="")
#     def __str__(self):
#         return self.eid + " : " + self.name + " : " + self.department.department
#         def getCountConfirm(self):
#             count = Confirms.objects.filter(employee=self).aggregate(count=Count('id'))
#             return count['count']
#
#         def getCountAccept(self):
#             count = Accepts.objects.filter(employee=self).aggregate(count=Count('id'))
#             return count['count']
#
#         def getCountSend(self):
#             count = Send.objects.filter(employee=self).aggregate(count=Count('id'))
#             return count['count']
# class Branch(models.Model):
#     bid = models.CharField(max_length=5,primary_key=True,default="")
#     branch = models.CharField(max_length=100,default="")
#     location = models.CharField(max_length=200, default="")
#     tel = models.CharField(max_length=10, default="")
#     def __str__(self):
#         return  self.bid+":"+self.branch
# #################################################################
# #อุปกรณ์เสริม
# class Accessories(models.Model):
#     aid = models.CharField(max_length=6, primary_key=True, default="")
#     name = models.CharField(max_length=50, default="")
#     price=models.FloatField(default=0.00)
#     net = models.IntegerField(default=0)
#     picture = models.ImageField(upload_to ='static/IMGproduct/', default="")
#     def __str__(self):
#         return self.aid + " : " + self.name
#     def getCountOrder(self):
#         count = OrderDetails.objects.filter(product=self).aggregate(count=Count('id'))
#         return count['count']
# #################################################################
# #ออเดอร์
# class Orders(models.Model):
#     oid = models.CharField(max_length=8, primary_key=True, default="")
#     odate = models.DateTimeField(auto_now_add = True)
#     customer = models.ForeignKey(Customers, on_delete=models.CASCADE, default=None)
#     status = models.CharField(max_length=1, default="")
#     def __str__(self):
#         return self.oid + " : " + str(self.odate.strftime("%Y-%m-%d")) + " : " + self.customer.name + " : " + str(self.getTotal()) + " : "+  self.getStatus()
#
#     def newOrderId(self):
#         #ord-yymm-xxxxxx
#         yy = str(datetime.date.today().strftime('%y'))
#         mm = str(datetime.date.today().strftime('%m'))
#         lastOrder = Orders.objects.last()
#         if lastOrder:
#             lastId = int(lastOrder.oid[9:])
#         else:
#             lastId = 0
#         id = str(lastId+1)
#         id=id.zfill(6)
#         newId  = "OD-"+ yy + mm + id
#         self.oid = newId
#
#     def getStatus(self):
#         if self.status == '1':
#             return 'Wait for Confirm (รอยืนยัน)'
#         elif self.status == '2':
#             return 'Wait for Money Transfer (รอการโอนเงิน)'
#         elif self.status == '3':
#             return 'Wait for Money Accept (รอรับเงินคืน)'
#         elif self.status == '4':
#             return 'Wait for Product Send (รอส่งสินค้า)'
#         elif self.status == '5':
#             return 'C o m p l e t e (เสร็จสมบูรณ์)'
#         elif self.status == '6':
#             return 'Order Cancel (ยกเลิกคำสั่งซื้อ)'
#         elif self.status == '7':
#             return 'Order Reject (ปฏิเสธคำสั่งซื้อ)'
#
#     def getOrderDetails(self):
#         orderDetails = OrderDetails.objects.filter(order=self)
#         return orderDetails
#
#     def getTotal(self):
#         total=OrderDetails.objects.filter(order=self).aggregate(total=Sum(F('oprice') * F('quantity')))
#         return total['total']
#
#     def getCount(self):
#         count= OrderDetails.objects.filter(order=self).aggregate(count=Count('id'))
#         return count['count']
#
# class OrderDetails(models.Model):
#     order=models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     accessories=models.ForeignKey(Accessories, on_delete=models.CASCADE, default=None)
#     oprice = models.FloatField(default=0.00)
#     quantity=models.IntegerField(default=1)
#     def __str__(self):
#         return self.order.oid + " : " + self.accessories.name + " : " + str(self.quantity)
#     def getTotal(self):
#         return self.oprice * self.quantity
# #################################################################
#
# class Confirms(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
#     cdate = models.DateTimeField(auto_now_add = True)
#     comment = models.CharField(max_length=200, default="")
#
# class Transfers(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     tdate = models.DateTimeField(auto_now_add = True)
#     reference = models.CharField(max_length=13, default="")
#     bank = models.CharField(max_length=50, default="")
#     bill = models.ImageField(upload_to ='static/bills/', default="")
#     comment = models.CharField(max_length=200, default="")
#
# class Accepts(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
#     adate =models.DateTimeField(auto_now_add = True)
#     comment = models.CharField(max_length=200, default="")
#
# class Send(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
#     sdate = models.DateTimeField(auto_now_add = True)
#     tag = models.CharField(max_length=50, default="")
#     comment = models.CharField(max_length=200, default="")
#
# class Cancel(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     cdate = models.DateTimeField(auto_now_add=True)
#     reason = models.CharField(max_length=200, default="")
#
# class Reject(models.Model):
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE, default=None)
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE, default=None)
#     rdate = models.DateTimeField(auto_now_add=True)
#     reason = models.CharField(max_length=200, default="")