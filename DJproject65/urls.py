from django.contrib import admin
from django.urls import path, include
from Express import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('news', views.news, name='news'),
    path('calculation', views.calculation, name='calculation'),

    # ลงทะเบียน & เข้าสู่ระบบ
    path('empNew', views.empNew, name='empNew'),
    path('cusRegister', views.cusRegister, name='cusRegister'),
    path('userLogin', views.userLogin, name='userLogin'),
    path('userLogout', views.userLogout, name='userLogout'),

    #Branch
    path('listBranch', views.listBranch, name='listBranch'),
    path('<branch_id>/oneBranch', views.oneBranch, name='oneBranch'),
    path('createBranch', views.createBranch, name='createBranch'),
    path('<str:branch_id>/updateBranch', views.updatebranch, name='updateBranch'),
    path('<branch_id>/gtdelBranch', views.gtdelBranch, name='gtdelBranch'),
    path('<str:branch_id>/delBranch', views.deleteBranch, name='delBranch'),

    # cus
    path('listCus', views.listCus, name='listCus'),
    path('<cid>/oneCus', views.oneCus, name='oneCus'),
    path('createCus', views.createCus, name='createCus'),
    path('<str:cid>/updateCus', views.updateCus, name='updateCus'),
    path('<cid>/gtdelCus', views.gtdelCus, name='gtdelCus'),
    path('<str:cid>/deleteCus', views.deleteCus, name='deleteCus'),

    # Emp
    path('listEmp', views.listEmp, name='listEmp'),
    path('<eid>/oneEmp', views.oneEmp, name='oneEmp'),
    path('createEmp', views.createEmp, name='createEmp'),
    path('<str:eid>/updateEmp', views.updateEmp, name='updateEmp'),
    path('<eid>/gtdelEmp', views.gtdelEmp, name='gtdelEmp'),
    path('<str:eid>/deleteEmp', views.deleteEmp, name='deleteEmp'),

    #Categories
    path('listCategories', views.listCategories, name='listCategories'),
    path('<cgid>/oneCategories', views.oneCategories, name='oneCategories'),
    path('createCategories', views.createCategories, name='createCategories'),
    path('<str:cgid>/updateCategories', views.updateCategories, name='updateCategories'),
    path('<cgid>/gtdelCategories', views.gtdelCategories, name='gtdelCategories'),
    path('<str:cgid>/delCategories', views.deleteCategories, name='delCategories'),

    #สินค้า
    path('createAcc', views.createAcc, name='createAcc'),
    path('listAcc', views.listAcc, name='listAcc'),
    path('<aid>/oneAcc', views.oneAcc, name='oneAcc'),
    path('<str:aid>/updateAcc', views.updateAcc, name='updateAcc'),
    path('<aid>/gtdelAcc', views.gtdelAcc, name='gtdelAcc'),
    path('<str:aid>/deleteAcc', views.deleteAcc, name='deleteAcc'),

    #Acc

    # path('<name>/oneAcc', views.oneAcc, name='oneAcc'),

    # path('<str:name>/updateAcc', views.updateAcc, name='updateAcc'),
    # path('<name>/gtdelAcc', views.gtdelAcc, name='gtdelAcc'),
    # path('<str:name>/delAcc', views.deleteAcc, name='delAcc'),


    


    # path('sv', views.service, name='sv'),


    path('shopping', views.shopping, name='shopping'),
    path('showBasket', views.showBasket, name='showBasket'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.order,name='order'),
    path('clearBasket', views.clearBasket, name='clearBasket'),
    #ออเดอร์
    path('<oid>/orderCancel', views.orderCancel, name='orderCancel'),
    path('<oid>/confirm', views.orderConfirm, name='confirm'),
    path('<oid>/transfer', views.transfers, name='transfer'),
    path('<oid>/accept', views.accept, name='accept'),
    path('<oid>/productSend', views.productSend, name='productSend'),

    path('<oid>/productSend', views.productSend, name='productSend'),





    path('<cid>/cusUpdate', views.cusUpdate, name='cusUpdate'),

    path('cusChangePassword', views.cusChangePassword, name='cusChangePassword'),

    #ลูกค้า
    path('allOrder', views.showAllOrder, name='allOrder'),
    path('<oid>/showOrderDetail', views.showOrderDetail, name='showOrderDetail'),


    # path('Express/', include('Express.urls')),
    # path('', views.home, name="home"),
    # path('header',views.header, name='header'),
    # path('menu',views.menu, name='menu'),

    path('warning', views.warning, name='warning'),
    path('question', views.question, name='question'),
    path('fast', views.fast, name='fast'),
    path('howto', views.howto, name='howto'),

    # path('sendLineMessage', views.sendLineMessage, name='sendLineMessage'),
]
