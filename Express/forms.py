from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('branch_id','name','location','tel',)
        widgets ={
            'branch_id':forms.TextInput(attrs={'class': 'form-control',  'size':8, 'maxlength':6}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'size': 13, 'maxlength': 10}),
        }
        lables ={
            'branch_id':'รหัสสาขา',
            'name': 'ชื่อสาขา',
            'location':'ที่ตั้ง',
            'tel': 'เบอร์ติดต่อ',
            }

        def updateForm(self):
            self.fields['branch_id'].widget.attrs['readonly'] = True
            self.fields['branch_id'].label = 'รหัสสาขา ไม่อนุญาติให้แก้ไข'

        def deleteForm(self):
            self.fields['branch_id'].widget.attrs['readonly'] = True
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['location'].widget.attrs['readonly'] = True
            self.fields['tel'].widget.attrs['readonly'] = True
class CategoiesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('cgid', 'name', 'desc')
        widgets = {
            'cgid': forms.TextInput(attrs={'class': 'form-control', 'size': 8, 'maxlength': 6}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'cgid': 'รหัสแผนก',
            'name': 'หมวดหมู่',
            'desc': 'รายละเอียดเพิ่มเติม',
        }
    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['desc'].widget.attrs['readonly'] = True
class EmployeesForm(forms.ModelForm):
    class Meta:
        STATUS_CHOICES = (
            ("Manager", "ผู้จัดการสาขา"),("CounterStaff", "พนักงานเคาท์เตอร์"),("Store", "พนักงานคลังสินค้า"),
            ("CallCenter", "พนักงาน Call center"),("Driver", "พนักงานขับรถ"),("Audit", "พนักงานบัญชี"),
        )
        GENDER_CHOICES = (
            ("Male", "เพศชาย"),
            ("Female", "เพศหญิง"),
        )
        model = Employees
        fields = ('name', 'gender','branch', 'position', 'birthdate', 'address', 'tel', 'eid')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':53, 'maxlength':50}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'birthdate':forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'size': 13, 'maxlength': 10}),
            'eid': forms.TextInput(attrs={'class': 'form-control', 'size': 23, 'maxlength': 20}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'size': 15, 'maxlength': 15}),
         }

        labels = {
            'name': 'ชื่อพนักงาน',
            'gender': 'เพศ',
            'branch': 'สาขา',
            'position': 'ตำแหน่ง',
            'birthdate': 'วัน/เดือน/ปีเกิด',
            'address': 'ที่อยู่',
            'tel': 'เบอร์โทรศัพท์',
            'eid': 'รหัสพนักงาน (Username)',
            'password': 'Password',

         }

    def updateForm(self):
        self.fields['eid'].widget.attrs['readonly'] = True
        self.fields['eid'].label = 'รหัสพนักงาน { ไม่อนุญาตให้แก้ไข }'

    def deleteForm(self):
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['branch'].widget.attrs['readonly'] = True
        self.fields['position'].widget.attrs['readonly'] = True
        self.fields['birthdate'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['tel'].widget.attrs['readonly'] = True
        self.fields['eid'].widget.attrs['readonly'] = True
class CustomersForm(forms.ModelForm):
    class Meta:
        GENDER_CHOICES = (
            ("Male", "เพศชาย"),
            ("Female", "เพศหญิง"),
        )
        model = Customers
        fields = ('name', 'gender', 'birthdate', 'address', 'tel', 'cid')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),
            'birthdate': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tel': forms.TextInput(attrs={'class': 'form-control','size':13, 'maxlength':10}),
            'cid': forms.TextInput(attrs={'class': 'form-control', 'size': 15, 'maxlength': 15}),

        }
        labels = {
            'name': 'ชื่อลูกค้า',
            'gender': 'เพศ',
            'birthdate': 'วัน/เดือน/ปีเกิด',
            'address': 'ที่อยู่',
            'tel': 'เบอร์โทรศัพท์',
            'cid': 'Username',
         }

    def updateForm(self):
        self.fields['cid'].widget.attrs['readonly'] = True
        self.fields['cid'].label=' User (ไม่อนุญาตให้แก้ไข!)'
class ServiceForm(forms.ModelForm):
    class Meta:
        # DIS_CHOICES = ( ("Muang", "อำเภอเมือง"),("Manchakiri", "มัญจาคีรี"),("Srechompu", "สีมพู")
        # )
        model = Servise
        fields = ('cus', 'person', 's_start', 's_end', 'type', 'weight')
        widgets = {
            'cus': forms.Select(attrs={'class': 'form-control'}),
            'person': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            's_start': forms.Select(attrs={'class': 'form-control'}),
            's_end': forms.Select(attrs={'class': 'form-control'}),
            'type' : forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cus' : 'ผุ้ส่ง',
            'person' : 'ผุ้รับ & ที่อยู่',
            's_start' : 'ต้นทาง',
            's_end' : 'ปลายทาง',
            'type' : 'รูปแบบพัสดุ',
            'weight' : 'น้ำหนัก (กิโลกรัม)'
         }




class AccessoriessForm(forms.ModelForm):
    class Meta:
        model = Accessoriess
        fields = ('category','aid', 'name', 'price', 'net')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'aid': forms.TextInput(attrs={'class': 'form-control',  'size':8, 'maxlength':6}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size':53, 'maxlength':50}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'Min': 1}),
            'net': forms.NumberInput(attrs={'class': 'form-control', 'Min': 0}),
        }
        labels = {
            'category': 'หมวดหมู่',
            'aid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'price': 'ราคาต่อหน่วย',
            'net': 'คงเหลือ',

        }

    def updateForm(self):
        self.fields['aid'].widget.attrs['readonly'] = True
        self.fields['aid'].label = 'รหัสสินค้า { ไม่อนุญาตให้แก้ไข }'

    def deleteForm(self):
        self.fields['aid'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['category'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['net'].widget.attrs['readonly'] = True
        self.fields['picture'].widget.attrs['readonly'] = True





class ChangePasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=20,
                             widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    oldPassword = forms.CharField(label='รหัสผ่านเดิม', max_length=15,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=15,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=15,
                                      widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ResetPasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=20,
                             widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=15,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=15,
                                      widget=forms.PasswordInput(attrs={'class':'form-control'}))

class TranfersForm(forms.ModelForm):
    class Meta:
        model = Transfers
        fields = ('order','reference', 'bank', 'bill')
        widgets = {
            'order': forms.HiddenInput(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control','size': 33, 'maxlength': 30}),
            'bank': forms.TextInput(attrs={'class': 'form-control','size': 53, 'maxlength': 50}),
            'bill': forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
        }
        labels = {
            'order': 'ใบสั่งซื้อสินค้า',
            'reference': 'หมายเลขใบโอนเงิน',
            'bank': 'จากธนาคาร',
            'bill': 'แนบไฟล์สลิป',
        }


class SendForm(forms.ModelForm):
    class Meta:
        model = Send
        fields = ('order','employee', 'barnch', 'tag')
        widgets = {
            'order': forms.HiddenInput(attrs={'class': 'form-control'}),
            'employee': forms.HiddenInput(attrs={'class': 'form-control'}),
            'barnch': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control', 'size': 53, 'maxlength': 50}),
        }
        labels = {
            'order': 'ใบสั่งซื้อสินค้า',
            'employee': 'พนักงาน',
            'barnch': 'ส่งจากสาขา',
            'tag': 'หมายเลขพัสดุ',
        }

class CancelForm(forms.ModelForm):
    class Meta:
        model = Cancel
        fields = ('order','reason')
        widgets = {
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'order': 'ใบสั่งซื้อสินค้า',
            'reason': 'แนบเหตุผลยกเลิกใบสั่งซื้อ',
        }

class RejectForm(forms.ModelForm):
    class Meta:
        model = Reject
        fields = ('order','employee', 'reason')
        widgets = {
            'order': forms.HiddenInput(attrs={'class': 'form-control'}),
            'employee': forms.HiddenInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'order': 'ใบสั่งซื้อสินค้า',
            'employee': 'พนักงาน',
            'reason': 'เหตุผลในการปฏิเสธการสั่งซื้อ',
        }

#
#
# class CustomersForm(forms.ModelForm):
#     class Meta:
#         model = Customers
#         fields = ('name', 'address', 'tel', 'cid', 'password')
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
#             'tel': forms.TextInput(attrs={'class': 'form-control','size':13, 'maxlength':10}),
#             'cid': forms.TextInput(attrs={'class': 'form-control', 'size': 20, 'maxlength': 20}),
#             'password':forms.TextInput(attrs={'class': 'form-control',   'size':10, 'maxlength':8}),
#         }
#         labels = {
#             'name': 'ชื่อ',
#             'address': 'ที่อยู่',
#             'tel': 'เบอร์โทรศัพท์',
#             'cid': 'User Name',
#             'password': 'Password',
#         }
#     def updateForm(self):
#         self.fields['cid'].widget.attrs['readonly'] = True
#         self.fields['cid'].label = 'User Name [ไม่อนุญาตให้แก้ไขได้]'
#
# ########################################
# class DepartmentsForm(forms.ModelForm):
#     class Meta:
#         model = Departments
#         fields = ('did', 'department','desc')
#         widgets ={
#             'did':forms.TextInput(attrs={'class':'form-control'}),
#             'department': forms.TextInput(attrs={'class': 'form-control','required':'required','max_length':35}),
#             'desc':forms.Textarea(attrs={'class':'form-control'}),
#         }
#         lables ={
#             'pid':'รหัสแผนก',
#             'department':'แผนก',
#             'desc': 'ลักษณะงาน',
#             }
# ########################################
# class EmployeesForm(forms.ModelForm):
#     class Meta:
#         model = Employees
#         fields = ('eid', 'name', 'birthdate', 'department', 'password')
#         widgets = {
#             'eid': forms.TextInput(attrs={'class': 'form-control', 'size':20, 'maxlength':20}),
#             'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
#             'birthdate':forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
#             'department': forms.Select(attrs={'class':'form-control'}),
#             'password':forms.TextInput(attrs={'class': 'form-control',  'size':10, 'maxlength':8}),
#         }
#         labels = {
#             'eid': 'รหัสพนักงาน',
#             'name': 'ชื่อพนักงาน',
#             'birthdate': 'วันเดือนปีเกิด',
#             'department': 'ตำแหน่ง',
#             'password' : 'รหัสผ่าน'
#         }
#
#     def updateForm(self):
#         self.fields['eid'].widget.attrs['readonly'] = True
#         self.fields['eid'].label = 'รหัสพนักงาน [ไม่อนุญาตให้แก้ไขได้]'
#         self.fields['password'].widget = forms.HiddenInput()
# ########################################

# ########################################
#
# class AccessoriesForm(forms.ModelForm):
#     class Meta:
#         model = Accessories
#         fields = ('aid', 'name','price', 'net', 'picture', )
#         widgets = {
#             'aid': forms.TextInput(attrs={'class': 'form-control',  'size':8, 'maxlength':6}),
#             'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'Min': 1}),
#             'net': forms.NumberInput(attrs={'class': 'form-control', 'Min': 0}),
#             'picture':forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
#         }
#         labels = {
#             'pid': 'รหัสสินค้า',
#             'name': 'ชื่อสินค้า',
#             'price': 'ราคาต่อหน่วย',
#             'net': 'คงเหลือ',
#             'picture': 'ภาพสินค้า',
#         }
#     def updateForm(self):
#         self.fields['aid'].widget.attrs['readonly'] = True
#         self.fields['aid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไข]'
# ########################################
#
# ###############################
#
# class ChangePasswordForm(forms.Form):
#     userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=8,
#                              widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
#     oldPassword = forms.CharField(label='รหัสผ่านเดิม', max_length=8,
#                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=8,
#                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=8,
#                                       widget=forms.PasswordInput(attrs={'class':'form-control'}))
# class ResetPasswordForm(forms.Form):
#     userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=8,
#                              widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
#     newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=8,
#                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=8,
#                                       widget=forms.PasswordInput(attrs={'class':'form-control'}))
# class TranfersForm(forms.ModelForm):
#     class Meta:
#         model = Transfers
#         fields = ('order','reference', 'bank', 'bill', 'comment')
#         widgets = {
#             'order': forms.HiddenInput(attrs={'class': 'form-control'}),
#             'reference': forms.TextInput(attrs={'class': 'form-control','size': 15, 'maxlength': 13}),
#             'bank': forms.TextInput(attrs={'class': 'form-control','size': 55, 'maxlength': 50}),
#             'bill': forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
#             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
#         }
#         labels = {
#             'order': 'ใบสั่งซื้อสินค้า',
#             'reference': 'หมายเลขใบโอนเงิน',
#             'bank': 'จากธนาคาร',
#             'bill': 'ไฟล์สลิปใบโอน',
#             'comment': 'หมายเหตุ ',
#         }
#     def setup(self):
#         self.fields['comment'].required = False
#
# class SendForm(forms.ModelForm):
#     class Meta:
#         model = Send
#         fields = ('order','employee', 'tag', 'comment')
#         widgets = {
#             'order': forms.HiddenInput(attrs={'class': 'form-control'}),
#             'employee': forms.HiddenInput(attrs={'class': 'form-control'}),
#             'tag': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
#             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
#         }
#         labels = {
#             'order': 'ใบสั่งซื้อสินค้า',
#             'employee': 'พนักงาน',
#             'tag': 'หมายเลขพัสดุ',
#             'comment': 'หมายเหตุ',
#         }
#
# class RejectForm(forms.ModelForm):
#     class Meta:
#         model = Reject
#         fields = ('order','employee', 'reason')
#         widgets = {
#             'order': forms.HiddenInput(attrs={'class': 'form-control'}),
#             'employee': forms.HiddenInput(attrs={'class': 'form-control'}),
#             'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
#         }
#         labels = {
#             'order': 'ใบสั่งซื้อสินค้า',
#             'employee': 'พนักงาน',
#             'reason': 'เหตุผลในการปฏิเสธการสั่งซื้อ',
#         }
