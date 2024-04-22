from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from flask import flash
from django.db.models import Q

from app5.models import *
from django.core.files.storage import FileSystemStorage
import datetime
import django.utils
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum,Count
import datetime

# Create your views here.

# ///////////////////////////////



def rpay(request):
    print("Haiiiiiiiii")
    
    

    # # Get the order ID
    # order_id = request.GET['order_id']
    # order_id = request.GET['order_id']
    # print(order_id)
    # s=booking.objects.get(id=id)
    # if s:
    #     s.status='Shipped'
    #     s.order_id=order_id
    #     s.save() 
    # od=bookingchild.objects.filter(booking_id=id)
    # print(od)
    # if od:
    #     for i in od:
    #         pid=i.product_id
    #         qtys=i.quantity
    #         print(pid,"....................proid")
    #         print(qtys,"..................qty")

    #         pp=product.objects.get(id=pid)
    #         # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
    #         if pp:
    #             pro_qty=pp.stock
    #             print(pro_qty,"############pro_qty")
    #             pp.stock=int(pro_qty)-int(qtys)
    #             pp.save()
    # return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")
   
    return render(request, 'orders.html')

def user_payment_complete(request,id,type,tt):

    if type == 'half':

        # print(order_id)
        s=booking.objects.get(booking_id=id)
        if s:
            s.status='advance paid'
            # s.order_id=id
            s.save() 
    if type == 'full':

        # print(order_id)
        s=booking.objects.get(booking_id=id)
        if s:
            s.status='payment completed'
            # s.order_id=id
            s.save() 
    
    # return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/userhome';</script>")
    return render(request,'toaster.html',{'message':'Payment Completed....!!!','location': '/userhome'})



def index(request):
    # view=profile.objects.all()
    view2=mywork.objects.all()
    view3=category.objects.all()

    cust_count = user.objects.filter(logins__usertype='user').count


    success=booking.objects.filter(status="completed").count()

    
    services = service.objects.all()
    if "searchsss" in request.POST:
        searchss=request.POST['searchss']
        servicesss = services.filter(categorys__category__icontains=searchss) | services.filter(service__icontains=searchss)
     
        print(servicesss)
   

    if "login" in request.POST:
        uname=request.POST['uname']
        password=request.POST['pass']
        print(uname)
        try:
            print("###############################")
            lg=login.objects.get(username=uname,password=password)
            print(lg)
            request.session['login_id']=lg.pk
            if lg.usertype == 'admin':
                # return HttpResponse("<script>alert('Login Success');window.location='/adminhome'</script>")
                return render(request,'toaster.html',{'message':'Login Successfull','location': '/adminhome'})
            elif lg.usertype == 'user':
                print("*******************************")
                uu=user.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['username']=uu.fname+" "+uu.lname
                request.session['user_id']=uu.pk
                
                return render(request,'toaster.html',{'message':'Login Successfull','location': 'userhome'})
            elif lg.usertype == 'studio':
                print("*******************************")
                uu=studio.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['username']=uu.studioname
                request.session['user_id']=uu.pk
                
                return render(request,'toaster.html',{'message':'Login Successfull','location': 'studiohome'})
            elif lg.usertype == 'photographer':
                print("*******************************")
                uu=photographer.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['username']=uu.fname+" "+uu.lname
                request.session['user_id']=uu.pk
                
                return render(request,'toaster.html',{'message':'Login Successfull','location': 'photographerhome'})
        except: 
            return render(request,'toaster.html',{'message':'Invalid Username Or Password','location': '/'})
            # return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/'</script>")
    
    if "register" in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pass']
       
        lg=login(username=username,password=password,usertype='pending')
        lg.save()
        
        user_reg1=user(fname=fname,lname=lname,place=place,phone=phone,email=email,logins=lg)
        user_reg1.save()
        
        
        # subject = 'Confirmation Link'
        # message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{lg.login_id}>verify</a>"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email, ]
        # send_mail( subject, message, email_from, recipient_list )
        
        # return HttpResponse("<script>alert('Successfully Added');window.location='/'</script>")
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/'})

    if "studioregister" in request.POST:
        names=request.POST['names']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        since=request.POST['since']
        license=request.POST['license']
        username=request.POST['uname']
        password=request.POST['pass']
       
        lg=login(username=username,password=password,usertype='pending')
        lg.save()
        
        studioreg=studio(studioname=names,place=place,phone=phone,email=email,since=since,licence=license,logins=lg)
        studioreg.save()
        
        
        # subject = 'Confirmation Link'
        # message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{lg.login_id}>verify</a>"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email, ]
        # send_mail( subject, message, email_from, recipient_list )
        
        # return HttpResponse("<script>alert('Successfully Added');window.location='/'</script>")
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/'})


    if "q" in request.POST:
        # print("Haiiiiii")
        sss=request.POST['q']
        view3=category.objects.filter(category=sss)


    return render(request,'public_section.html',{'services': services,'view2': view2,'view3': view3,'user':cust_count,'completed':success})


def public_view_category(request,id):
    view1=category.objects.filter(id=id)
    
    return render(request,'public_view_category.html',{'view3':view1})






def login_page(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        print(uname)
        try:
            print("###############################")
            lg=login.objects.get(username=uname,password=password)
            print(lg)
            request.session['login_id']=lg.pk
            if lg.usertype == 'admin':
                return HttpResponse("<script>alert('Login Success');window.location='/adminhome'</script>")
            
            elif lg.usertype == 'user':
                print("*******************************")
                uu=user.objects.get(logins_id=request.session['login_id'])
                print(uu)
                request.session['user_id']=uu.pk
                
                return HttpResponse("<script>alert('Login Success');window.location='/userhome'</script>")
        except:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/login'</script>")
        
    return render(request,'login.html')

def user_reg(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pass']
       
        lg=login(username=username,password=password,usertype='pending')
        lg.save()
        
        user_reg1=user(fname=fname,lname=lname,place=place,phone=phone,email=email,logins=lg)
        user_reg1.save()
        
        
        
        return HttpResponse("<script>alert('Successfully Added');window.location='/login'</script>")

    return render(request,'user_registration.html')


def acceptcustomer_username(request,id):
    cus=login.objects.get(login_id=id)
    cus.usertype='user'
    cus.save()
    # return HttpResponse("<script>alert('Verified');window.location='/'</script>")
    return render(request,'toaster.html',{'message':'Verified','location': '/'})

#################################### ADMIN SECTION ################################################################


def admin_home(request):
    studio_count = studio.objects.filter(logins__usertype='studio').count
    photographer_count = photographer.objects.filter(logins__usertype='photographer').count
    cust_count = user.objects.filter(logins__usertype='user').count
    catg = category.objects.all().count

   
    return render(request,'admin_home.html',{'stud':studio_count,'photog':photographer_count,'cust':cust_count,'catg':catg})

# def admin_upload_profile(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         details=request.POST['details']
#         since=request.POST['since']
#         lice=request.POST['lice']
#         up_prof=profile(name=name,details=details,since=since,licence=lice)
#         up_prof.save()
#     view=profile.objects.all()
#     return render(request,'admin_upload_profile.html',{'view':view})

# def update_profile(request,profile_id):
#     upd_prof=profile.objects.get(profile_id=profile_id)
#     if request.method=='POST':
#         name=request.POST['name']
#         details=request.POST['details']
#         since=request.POST['since']
#         lice=request.POST['lice']
#         upd_prof.namey=name
#         upd_prof.details=details
#         upd_prof.since=since
#         upd_prof.licence=lice
#         upd_prof.save()
#         # return HttpResponse("<script>alert('Successfully Updated');window.location='/adminuploadprofile'</script>")
#         return render(request,'toaster.html',{'message':'Successfully Updated','location': '/adminuploadprofile'})

#     return render(request,'admin_upload_profile.html',{'upd_prof':upd_prof})


def admin_view_user(request):
    view=user.objects.all()
    return render(request,'admin_view_user.html',{'view':view})

def updateusertoblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="blocked"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewuser'})

def updateusertounblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="user"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewuser'})

def updateusertoaccept(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="user"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewuser'})

def updateusertoreject(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="reject"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewuser'})

    # return render(request,'admin_manage_category.html',{'upd_cate':upd_cate})

def admin_view_studio(request):
    view=studio.objects.all()
    return render(request,'admin_view_studio.html',{'view':view})

def updatestudiotoaccept(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="studio"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewstudio'})

def updatestudiotoreject(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="reject"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewstudio'})

def updatestudiotoblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="blocked"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewstudio'})

def updatestudiotounblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="studio"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewstudio'})


def admin_view_photographer(request):
    view=photographer.objects.all()
    return render(request,'admin_view_photographer.html',{'view':view})

def updatephototoblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="blocked"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewphotographer'})

def updatephototounblock(request,lid):
    updtoblock=login.objects.get(login_id=lid)    
    updtoblock.usertype="photographer"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/viewphotographer'})


def admin_manage_category(request):
    if request.method=='POST':
        man_cate=request.POST['cate']
        image=request.FILES['img']
        fs = FileSystemStorage()
        f_nam = fs.save(image.name, image)
        add_cate=category(category=man_cate,image=f_nam)
        add_cate.save()
        
    view=category.objects.all()
    return render(request,'admin_manage_category.html',{'view':view})

def update_category(request,category_id):
    upd_cate=category.objects.get(category_id=category_id)
    if request.method=='POST':
        cate=request.POST['cate']
        upd_cate.category=cate
        upd_cate.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/managecategory'})

    return render(request,'admin_manage_category.html',{'upd_cate':upd_cate})

def delete_category(request,category_id):
    dele_cate=category.objects.get(category_id=category_id)
    dele_cate.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/managecategory'})
    
        
def admin_view_bookings(request):
    if "search" in request.POST:
        # print("Haiiiii")
        dates=request.POST['dates']
        print(dates)
        view=booking.objects.filter(date=dates)
        print(view)
    else:
        view=booking.objects.all()
    return render(request,'admin_view_bookings.html',{'view':view})


    

def admin_view_feedback(request):
    view=feedback.objects.all()
    
    return render(request,'admin_view_feedback.html',{'view':view})

def admin_view_rated(request,pid):
    
    view=review.objects.filter(photographers_id=pid)
    return render(request,'admin_view_rated.html',{'view':view})


    
    # return render(request,'admin_upload_profile.html',{'view':view})

def admin_update_profile(request,profile_id):
    up_profile=profile.objects.get(profile_id=profile_id)
    if request.method=='POST':
        name=request.POST['name']
        details=request.POST['details']
        since=request.POST['since']
        lice=request.POST['lice']
        up_profile.name=name
        up_profile.details=details
        up_profile.since=since
        up_profile.licence=lice
        up_profile.save()
        # return HttpResponse("<script>alert('profile Updated successfully');window.location='/adminupdateprofile'</script>")
        return render(request,'admin_upload_profile.html',{'message':'profile Updated successfully','location': 'userhome'})
        
    return render(request,"admin_upload_profile.html")

def admin_view_complaints(request):
    
    view1=complaints.objects.all()
    return render(request,'admin_view_complaints.html',{'view':view1})

def admin_send_reply(request,cid):
    
    if request.method=='POST':
        view1=complaints.objects.get(complaint_id=cid)
        reply=request.POST['reply']
        view1.reply=reply
        view1.save()
        return render(request,'toaster.html',{'message':'Successfully Removed','location': '/admin_view_complaints'})
    return render(request,'admin_send_reply.html')

# def admin_view_report(request):
#     if "search" in request.POST:
#         # print("Haiiiii")
#         dates=request.POST['dates']
#         print(dates)
#         view=booking.objects.filter(date=dates)
#         print(view)
#     else:
#         view=payment.objects.all()
#     return render(request,'admin_view_report.html',{'view':view})



def admin_view_report(request):
    if request.method == 'POST':
        from_date_str = request.POST['from_date']
        to_date_str = request.POST['to_date']

        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
            reports = booking.objects.filter(date__range=[from_date_str, to_date_str])
            print("reportxxx", reports)
          
        else:
            reports = booking.objects.all()
           

        return render(request, 'admin_view_report.html', {'view': reports})
    else:
        reports = booking.objects.all()
      
    return render(request, 'admin_view_report.html', {'view': reports})

    

def admin_view_camara_report(request):
    if request.method == 'POST':
        from_date_str = request.POST['from_date']
        to_date_str = request.POST['to_date']
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
            reports = requests.objects.filter(date__range=[from_date_str, to_date_str])
            print("reportxxx", reports)
        else:
            reports = requests.objects.all()
        return render(request, 'admin_view_camara_report.html', {'view': reports})
    else:
        reports = requests.objects.all()
    return render(request, 'admin_view_camara_report.html', {'view': reports})

############################################## user section #############################################################




def user_view_potcategory(request,pid):
    view1=category.objects.filter(protfolio__photographers_id=pid).distinct()
    print("jjjjjjjjjjjjjjjjj",view1)
    
    return render(request,'user_view_potcategory.html',{'view3':view1,'pid':pid})



def user_home(request):
    view1=category.objects.all()
    if "q" in request.POST:
        # print("Haiiiiii")
        sss=request.POST['q']
        view1=category.objects.filter(category=sss)
    return render(request,'user_home.html',{'username':request.session['username'],'view3':view1})

def userupdateprofile(request):
    view1=user.objects.filter(user_id=request.session['user_id'])
    print(view1)
    if "submit" in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        bb=user.objects.get(user_id=request.session['user_id'])
        bb.fname=fname
        bb.lname=lname
        bb.place=place
        bb.phone=phone
        bb.email=email
        bb.save()
    
    return render(request,'userupdateprofile.html',{'view3':view1})

def user_view_service(request,id):
    query = request.GET.get('q', '')
    services = service.objects.filter(categorys_id=id)
    if query:
        services = services.filter(categorys__category__icontains=query) | services.filter(service__icontains=query)
    return render(request, 'user_view_service.html', {'services': services})
 

def user_book_service(request,service_id,amount):
    from datetime import datetime
    from datetime import date
    today=datetime.now()
    formatted_datetime = today.strftime('%Y-%m-%d %H:%M')
    print(today)
    us_bo= service.objects.get(service_id=service_id)
    print(us_bo.studios_id)
    us_ph= photographer.objects.filter(studios_id=us_bo.studios_id)
    print(us_ph)
    if request.method=='POST':
        venue = request.POST['venue']
        place = request.POST['place']
        datess = request.POST['date']
        time = request.POST['time']
        sph = request.POST['sph']
        ui_d=request.session['user_id']
        
        qr=booking.objects.filter(photographers_id=sph,bookingfordate=datess)
        if qr:
            return HttpResponse("<script>alert('Photographer Not Avaibale');window.location='/user_view_category'</script>")
        else: 
            serv_book=booking(pref=sph,venue=venue, place=place, date=formatted_datetime,bookingfordate=datess, status='pending',services_id=service_id,users_id=ui_d,time=time,amounts=amount,photographers_id=sph)
            serv_book.save()
            return render(request,'toaster.html',{'message':'Booking completed successfully','location': 'user_home'})
        return HttpResponse("<script>alert('Booking completed successfully');window.location='/user_view_category'</script>")
    return render(request,'user_book_service.html',{'us_bo':us_bo,'us_ph':us_ph,'today':str(today)})


    

def user_view_booking(request):
    view=booking.objects.filter(users_id=request.session['user_id'])
    return render(request,'user_view_booking.html',{'view':view})

def make_advance_payment(request,booking_id):
    bo_id=booking.objects.get(booking_id=booking_id)

    amt=int(bo_id.amounts)/2
    print(amt)
    if request.method=='POST':
        amt=request.POST['amount']
        date=datetime.today()
        
        ad_py=payment(amount=amt,date=date,bookings_id=booking_id)
        ad_py.save()
        bo_id.status='advance paid'
        bo_id.save()
        return render(request,'toaster.html',{'message':'Half Amount Successfully Payed ','location': '/userviewbooking'})
        # return render(request,'user_view_booking.html',{'message':'payment process completed','location': 'userhome'})
        # return HttpResponse("<script>alert('payment process completed');window.location='/userviewbooking'</script>")
    return render(request,'user_make_advance_payment.html',{'bo_id':bo_id,'amt':amt})

import datetime
def make_full_payment(request, booking_id):
    acc_pay = payment.objects.get(bookings_id=booking_id) 
    book = booking.objects.get(booking_id=booking_id)
    serv = service.objects.get(service_id=book.services_id)
    diff = float(book.amounts) - float(acc_pay.amount)
    if request.method == 'POST':
        fl_amt = request.POST['amount']
        
        
        # diff = float(serv.amount) - float(acc_pay.amount)
        # add = int(acc_pay.amount) + diff
        
        date = datetime.today()
    
        ad_py=payment(amount=fl_amt,date=date,bookings_id=booking_id)
        ad_py.save()
        book.status='payment completed'
        book.save()
        # return HttpResponse("<script>alert('payment completed');window.location='/userviewbooking'</script>")
        return render(request,'toaster.html',{'message':'Full Amount Successfully Payed ','location': '/userviewbooking'})
            # return HttpResponse("<script>alert('your balance amount is not matching');window.location='/userviewbooking'</script>")
            
    return render(request, 'user_make_advance_payment.html', {'acc_pay': acc_pay,'diff':diff})

def view_uploaded_video(request,booking_id):
    
    view=uploads.objects.filter(bookingss_id=booking_id)

    return render(request,'user_view_uploaded_video.html',{'view':view})


def user_view_work(request,id):
    view=mywork.objects.filter(category_id=id)
    
    return render(request,'user_view_work.html',{'view1':view})

def user_view_category(request):
    view1=category.objects.all()
    
    return render(request,'user_view_category.html',{'view3':view1})

def user_add_feedback(request):
    if request.method=='POST':
        us_feedback=request.POST['feedback']
        dates=date.today()
        feed_back=feedback(users_id=request.session['user_id'],feedback=us_feedback,date=dates)
        feed_back.save()
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/useraddfeedback'})

    return render(request,'user_add_feedback.html')

def user_add_complants(request):
    if request.method=='POST':
        complaint=request.POST['complaint']
        dates=date.today()
        feed_back=complaints(users_id=request.session['user_id'],complaints=complaint,reply="NA",date=dates)
        feed_back.save()
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/user_add_complants'})
    view1=complaints.objects.filter(users_id=request.session['user_id'])
    return render(request,'user_add_complaints.html',{'view':view1})

def user_add_rating(request,pid):
    if request.method=='POST':
        rates=request.POST['r']
        reviews=request.POST['review']
        dates=date.today()
        feed_back=review(users_id=request.session['user_id'],rate=rates,review=reviews,date=dates,photographers_id=pid)
        feed_back.save()
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/user_add_rating/%s' %(pid)})
    view=review.objects.filter(users_id=request.session['user_id'])
    return render(request,'user_add_rating.html',{'view':view})

def user_view_photographer(request):
    if request.method=='POST':
        check=request.POST['check']
        vals=request.POST['vals']
        print(check)
        if check=="Name":
            view=photographer.objects.filter(logins__usertype="photographer",fname__contains=vals) | photographer.objects.filter(studios__studioname__icontains=vals)
        elif check=="Place":
            view=photographer.objects.filter(logins__usertype="photographer",place__contains=vals)| photographer.objects.filter(studios__place__icontains=vals)
        elif check=="Pincode":
            view=photographer.objects.filter(logins__usertype="photographer",pincode__contains=vals)
    else:
        view=photographer.objects.filter(logins__usertype="photographer")
    return render(request,'user_view_photographer.html',{'view':view})

def user_assigned_photographer(request,bid):
    bass=assignphoto.objects.get(bookings_id=bid)
    view=photographer.objects.filter(photographer_id=bass.photographers_id)
    return render(request,'user_assigned_photographer.html',{'view':view})


def user_view_camera(request):
    if request.method=='POST':
        # check=request.POST['check']
        vals=request.POST['vals']
        # print(check)
        # if check=="Name":
        view=camera.objects.filter(camera__icontains=vals)|camera.objects.filter(sensortypeandsize__icontains=vals)|camera.objects.filter(lensetype__icontains=vals)|camera.objects.filter(studios__studioname__icontains=vals)
        # elif check=="Place":
        #     view=photographer.objects.filter(logins__usertype="photographer",place__contains=vals)
        # elif check=="Pincode":
        #     view=photographer.objects.filter(logins__usertype="photographer",pincode__contains=vals)
    else:
        view=camera.objects.all()
    return render(request,'user_view_camera.html',{'view':view })


def user_send_request(request,cid):
    # if request.method=='POST':
    # cid=request.get['cid']
    dates=date.today()
    sendreq=requests(users_id=request.session['user_id'],cameras_id=cid,date=dates,status='pending')
    sendreq.save()
    return render(request,'toaster.html',{'message':'Request Send Successfully ','location': '/user_view_camera'})

def user_view_request(request):
    
    view=requests.objects.filter(users_id=request.session['user_id'])
    return render(request,'user_view_request.html',{'view':view }) 

def user_view_protolio(request,pid,category_id):
    
    view=protfolio.objects.filter(photographers_id=pid,category_id=category_id)
    print(view)
    return render(request,'user_view_protolio.html',{'view':view })


def userreturncamera(request,rid):
    rej_book=requests.objects.get(request_id=rid)
    rej_book.status="Return and Paid"
    rej_book.save()
    updtoblock=camera.objects.get(camera_id=rej_book.cameras_id)    
    updtoblock.status="Available"
    updtoblock.save()
    
    # return HttpResponse("<script>alert('successfully rejected');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'Accepted successfully','location': '/user_view_request'})


def user_make_chat(request,pid):
    if request.method=='POST':
        chats=request.POST['chat']
        dates=date.today()
        feed_back=chat(sender_id=request.session['login_id'],receiver_id=pid,message=chats,date=dates)
        feed_back.save()
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/user_make_chat/%s' %(pid)})
    view=chat.objects.filter(Q(sender_id=request.session['login_id'],receiver_id=pid) | Q(sender_id=pid,receiver_id=request.session['login_id']))
    return render(request,'user_make_chat.html',{'view':view,'uid':request.session['login_id']})


def user_view_studio(request,sid):
    
    view=studio.objects.filter(studio_id=sid)
    print(view)
    return render(request,'user_view_studio.html',{'view':view })


#########################################public#######################################################################

def public_view_service(request,category_id):
    print(category_id)
    query = request.GET.get('q', '')
    services = service.objects.filter(categorys_id=category_id)
    if query:
        services = services.filter(categorys__category__icontains=query) | services.filter(service__icontains=query)
    return render(request, 'public_view_services.html', {'services': services})

def public_view_myworks(request,sid):
    view=mywork.objects.filter(category_id=sid)
    print(view)
    return render(request, 'public_view_myworks.html',{'view1':view})


   


def public_view_studios(request,sid):
    
    view=studio.objects.filter(studio_id=sid)
    print(view)
    return render(request,'public_view_studios.html',{'view':view })

from datetime import * 

def user_make_payment(request,id,type):
    today=date.today()
    print(today)
    print(">>>>>>>>>>>>>>>>",type)

    q=booking.objects.get(booking_id=id)
    print(q)
    print(q.amounts) 
    s=int(q.amounts)
    half = s/2
    ss={}
   
    ss['total']=type
    return render(request,'user_make_payment.html',{'type':type,'ids':id,'total':half})








def forgot(request):
    if request.method=="POST":
        unamee=request.POST['uname']
        phone=request.POST['ph']
        # try:
        ob=login.objects.get(username=unamee)
        print("###################################")
        print(ob)
        if ob:
            request.session['llid']=ob.pk
            ob1=user.objects.filter(phone=phone,logins_id=ob.pk)
            print(ob1)
            if ob1: 
                import random
                number = random.randint(1111,9999)
                request.session['otp']=number
                print(number)        
                for i in ob1:
                    print(i.email)
                    subject = 'One Time Password'
                    message = f"sir,\n One Time Password :"+ str(number)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [i.email, ]
                    send_mail( subject, message, email_from, recipient_list )
                        
                    return HttpResponse('''<script>alert("mail sended");window.location='otp'</script>''')   
            else:
                return HttpResponse('''<script>alert("Invalid Details");window.location='/'</script>''') 
        # except Exception:
        #     return HttpResponse('''<script>alert("Invalid Details");window.location='/'</script>''') 
    return render(request,'forgotpass.html')  



def otp(request):
    # print("##############")
    if request.method=="POST":
        otpnum=int(request.POST['otpp'])
        # print("SSSS : ",otpnum)

        ottp=int(request.session['otp'])
        # print("*******")
        # print("UUUUUUUUUUU",ottp)
        if ottp==otpnum:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return HttpResponse('''<script>alert("Success");window.location='newpas'</script>''') 

    return render(request, 'optmsg.html') 


def newpas(request):
    lo=login.objects.get(pk=request.session['llid'])
    if request.method=="POST":
        npass=request.POST['passw']
        cpass=request.POST['cpassw']
       
        lo.password=npass
        lo.save()
        return HttpResponse('''<script>alert("confirm");window.location='/'</script>''')   
    return render(request, 'newpass.html')



# /////////////////////////////////////////////////  Studio Section ///////////////////////////////////////////


def studio_home(request):
    names=request.session['username']
    print(names)
    sid=request.session['user_id']
    photographer_count = photographer.objects.filter(studios_id=sid).count
    wrk = mywork.objects.filter(studios_id=sid).count
    # photographer_count = photographer.objects.filter(studios_id=sid).count
    view=booking.objects.filter(services__studios__studio_id=request.session['user_id']).count
    camara=requests.objects.filter(cameras__studios__studio_id=request.session['user_id']).count
   
    return render(request,'studio_home.html',{'photog':photographer_count,'wrk':wrk,'names':names,'view':view,'camara':camara})


def studio_update_profile(request):
    sid=request.session['user_id']
    upd_prof=studio.objects.get(studio_id=sid)
    if request.method=='POST':
        name=request.POST['name']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        since=request.POST['since']
        lice=request.POST['lice']
        upd_prof.studioname=name
        upd_prof.place=place
        upd_prof.phone=phone
        upd_prof.email=email
        upd_prof.since=since
        upd_prof.licence=lice
        upd_prof.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/adminuploadprofile'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_update_profile'})

    return render(request,'studio_update_profile.html',{'upd_prof':upd_prof})

def studio_manage_photographer(request):
    if request.method=='POST':
        ss=studio.objects.get(studio_id=request.session['user_id'])
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        pincode=request.POST['pincode']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        # fs = FileSystemStorage()
        # f_nam = fs.save(image.name, image)
        lg=login(username=username,password=password,usertype='photographer')
        lg.save()
        addphoto=photographer(fname=fname,lname=lname,place=place,phone=phone,pincode=pincode,email=email,logins=lg,studios=ss)
        addphoto.save()
        
    # vi_cat=category.objects.all()
    view=photographer.objects.filter(studios_id=request.session['user_id'])
   
    
    return render(request,'studio_manage_photographer.html',{'view':view })



def studiodeletephotographer(request,lid):
    dele_photo=photographer.objects.get(logins_id=lid)
    dele_photo.delete()
    dele_photol=login.objects.get(login_id=lid)
    dele_photol.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/studio_manage_photographer'})


def studio_manage_camera(request):
    if request.method=='POST':
        ss=studio.objects.get(studio_id=request.session['user_id'])
        cameras=request.POST['camera']
        apd=request.POST['apd']
        res=request.POST['res']
        sensor=request.POST['sensor']
        lense=request.POST['lense']
        connection=request.POST['connection']
        xxx = request.FILES['imgxxxxxx']
        fss = FileSystemStorage()
        fn = fss.save(xxx.name, xxx)
        addphoto=camera(amountperday=apd,camera=cameras,resolution=res,sensortypeandsize=sensor,lensetype=lense,connectiontype=connection,status="Available",studios=ss,cam_img=fn)
        addphoto.save()
        
    # vi_cat=category.objects.all()
    view=camera.objects.filter(studios_id=request.session['user_id'])
    return render(request,'studio_manage_camera.html',{'view':view })

def studioupdatecamera(request,cid):
    upd_cate=camera.objects.get(camera_id=cid)
    if request.method=='POST':
        cameras=request.POST['camera']
        res=request.POST['res']
        sensor=request.POST['sensor']
        lense=request.POST['lense']
        connection=request.POST['connection']
        apd=request.POST['apd']
        upd_cate.camera=cameras
        upd_cate.resolution=res
        upd_cate.sensortypeandsize=sensor
        upd_cate.lensetype=lense
        upd_cate.connectiontype=connection
        upd_cate.amountperday=apd
        upd_cate.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_manage_camera'})

    return render(request,'studio_manage_camera.html',{'upd_cate':upd_cate})

def studiodeletecamera(request,cid):
    dele_cate=camera.objects.get(camera_id=cid)
    dele_cate.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/studio_manage_camera'})

def studionotavilablecamera(request,cid):
    updtoblock=camera.objects.get(camera_id=cid)    
    updtoblock.status="Not Available"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_manage_camera'})

def studioavilablecamera(request,cid):
    updtoblock=camera.objects.get(camera_id=cid)   
    updtoblock.status="Available"
    updtoblock.save()
    # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_manage_camera'})


def studio_manage_service(request):
    if request.method=='POST':
        ss=studio.objects.get(studio_id=request.session['user_id'])
        man_serv=request.POST['service']
        man_cate=request.POST['cate']
        man_amt=request.POST['amount1']
        man_details=request.POST['details']
        image=request.FILES['img']
        fs = FileSystemStorage()
        f_nam = fs.save(image.name, image)
        add_serv=service(service=man_serv,categorys_id=man_cate,amount=man_amt,details=man_details,image=f_nam,studios=ss)
        add_serv.save()
        
    vi_cat=category.objects.all()
    view=service.objects.filter(studios_id=request.session['user_id'])
   
    
    return render(request,'studio_manage_service.html',{'view':view , 'vi_cat':vi_cat})

def update_service(request, service_id):
    upd_serv = service.objects.get(service_id=service_id)
    categories = category.objects.all()
    if request.method == 'POST':
        man_serv = request.POST['ser']
        man_cate = request.POST['cate']
        man_amt = request.POST['amount']
        man_details = request.POST['details']
        upd_serv.service = man_serv
        upd_serv.category_id = man_cate
        upd_serv.amount = man_amt
        upd_serv.details = man_details
        upd_serv.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/manageservice'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_manage_service'})

    return render(request, 'studio_manage_service.html', {'upd_serv': upd_serv,'categories':categories})


def delete_service(request,service_id):
    dele_serv=service.objects.get(service_id=service_id)
    dele_serv.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/manageservice'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/studio_manage_service'})

def studio_add_myworks(request):
    q=category.objects.all()
    if request.method=='POST':
        ss=studio.objects.get(studio_id=request.session['user_id'])
        pu_wo=request.POST['works']
        ser=request.POST['ser']
        uploaded_video=request.FILES['upload']
        fs = FileSystemStorage()
        f_nam = fs.save(uploaded_video.name, uploaded_video)
        # pu_ty=request.POST['type']
        up_myworks=mywork(works=pu_wo,files=f_nam,type=uploaded_video.content_type,category_id=ser,studios=ss)
        up_myworks.save()
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_add_myworks'})
    view1=mywork.objects.filter(studios_id=request.session['user_id'])
    return render(request,'studio_add_myworks.html',{'view1':view1,'q':q})

def studio_remove_works(request,id):
    pro_del=mywork.objects.get(mywork_id=id)
    pro_del.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/addmywork'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/studio_add_myworks'})


def studio_view_bookings(request):
    ss=studio.objects.get(studio_id=request.session['user_id'])
    if "search" in request.POST:
        # print("Haiiiii")
        dates=request.POST['dates']
        print(dates)
        view=booking.objects.filter(date=dates,services__studios__studio_id=request.session['user_id'])
        print(view)
    else:
        view=booking.objects.filter(services__studios__studio_id=request.session['user_id'])
    return render(request,'studio_view_bookings.html',{'view':view})


def studio_view_booking_report(request):
    ss=studio.objects.get(studio_id=request.session['user_id'])
    if "search" in request.POST:
        # print("Haiiiii")
        dates=request.POST['dates']
        print(dates)
        view=booking.objects.filter(date=dates,services__studios__studio_id=request.session['user_id'])
        print(view)
    else:
        view=booking.objects.filter(services__studios__studio_id=request.session['user_id'])
    return render(request,'studio_view_booking_report.html',{'view':view})



def studio_payed_offline(request,bid):
    acc_book=booking.objects.get(booking_id=bid)
    acc_book.status='payment completed'
    acc_book.save()

    # fl_amt = request.POST['amount']
        
    # date = datetime.today()

    # ad_py=payment(amount=fl_amt,date=date,bookings_id=booking_id)
    # ad_py.save()
    # book.status='payment completed'
    # book.save()
    
    # return HttpResponse("<script>alert('successfully updated');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/studio_view_bookings'})


def studio_update_booking_status(request,booking_id):
    acc_book=booking.objects.get(booking_id=booking_id)
    acc_book.status='completed'
    acc_book.save()
    
    # return HttpResponse("<script>alert('successfully updated');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'Successfully Updated','location': '/photographer_view_bookings'})

def studio_view_advance_payment(request,booking_id):
    view=payment.objects.filter(bookings_id=booking_id)
    return render(request,'studio_view_advance_payment.html',{'view':view})

def studio_view_photographers(request,booking_id,bookingfordate):
    ss=studio.objects.get(studio_id=request.session['user_id'])
    view=photographer.objects.filter(studios=ss)
    return render(request,'studio_view_photographers.html',{'view':view,'bid':booking_id,'bdate':bookingfordate})

def studio_accept_booking(request,pid,bid,bdate):
    qr=assignphoto.objects.filter(photographers_id=pid,bookings_id=bid)
    if qr:
        return HttpResponse("<script>alert('Photographer Not Avaibale');window.location='/studio_view_bookings'</script>")
    else:
        acc_booking=booking.objects.get(booking_id=bid)
        acc_booking.status='accepted'
        acc_booking.save()
        acc_ph=photographer.objects.get(photographer_id=pid)
        acceptsss=assignphoto(bookings=acc_booking,photographers=acc_ph)
        acceptsss.save()
        
    # return HttpResponse("<script>alert('successfully accepted');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'successfully Accepted','location': '/studio_view_bookings'})

def studio_reject_booking(request,booking_id):
    rej_book=booking.objects.get(booking_id=booking_id)
    rej_book.status="booking denied"
    rej_book.save()
    # return HttpResponse("<script>alert('successfully rejected');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'successfully rejected','location': '/studio_view_bookings'})    



def studio_upload_video(request, booking_id):
    booking_obj = booking.objects.get(booking_id=booking_id)
    if request.method == 'POST':
        uploaded_video = request.FILES['file']
        
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_video.name, uploaded_video)
        video_type = request.POST['type']
        upload_obj = uploads(file=file_name, type=video_type, bookingss=booking_obj)
        upload_obj.save()
        # return HttpResponse("<script>alert('Upload completed');window.location='/viewbookings'</script>")
        return render(request,'toaster.html',{'message':'successfully Uploaded','location': '/studio_view_bookings'})    

        
    return render(request,'studio_upload_video.html')

def studio_view_request(request):
    # ss=studio.objects.get(studio_id=request.session['user_id'])
    view=requests.objects.filter(cameras__studios__studio_id=request.session['user_id'])
    return render(request,'studio_view_request.html',{'view':view }) 

def studio_view_camara_report(request):
    # ss=studio.objects.get(studio_id=request.session['user_id'])
    view=requests.objects.filter(cameras__studios__studio_id=request.session['user_id'])
    return render(request,'studio_view_camara_report.html',{'view':view }) 




def studio_accept_request(request,rid):
    rej_book=requests.objects.get(request_id=rid)
    rej_book.status="Accept"
    rej_book.save()
    updtoblock=camera.objects.get(camera_id=rej_book.cameras_id)    
    updtoblock.status="Not Available"
    updtoblock.save()
    
    # return HttpResponse("<script>alert('successfully rejected');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'Accepted successfully','location': '/studio_view_request'})  


def studio_reject_request(request,rid):
    rej_book=requests.objects.get(request_id=rid)
    rej_book.status="Reject"
    rej_book.save()
    # return HttpResponse("<script>alert('successfully rejected');window.location='/viewbookings'</script>")
    return render(request,'toaster.html',{'message':'successfully rejected','location': '/studio_view_request'})  

def studio_view_rated(request,pid):
    
    view=review.objects.filter(photographers_id=pid)
    return render(request,'studio_view_rated.html',{'view':view})

# ///////////////////////////////////////////// Photographer ////////////////////////////////////////


def photgrapher_home(request):
    names=request.session['username']
    print(names)
    pid=request.session['user_id']

   
    return render(request,'photgrapher_home.html',{'names':names})

def photographer_update_profile(request):
    sid=request.session['user_id']
    upd_prof=photographer.objects.get(photographer_id=sid)
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        upd_prof.fname=fname
        upd_prof.lname=lname
        upd_prof.place=place
        upd_prof.phone=phone
        upd_prof.email=email
        upd_prof.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/adminuploadprofile'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/photographer_update_profile'})

    return render(request,'photographer_update_profile.html',{'upd_prof':upd_prof})


def photographer_manage_articles(request):
    if request.method=='POST':
        sid=request.session['user_id']
        pid=photographer.objects.get(photographer_id=sid)
        arti=request.POST['arti']
        details=request.POST['details']
        
        add_arti=article(article=arti,details=details,photographers=pid)
        add_arti.save()
        
    view=article.objects.all()
    return render(request,'photographer_manage_articles.html',{'view':view})

def update_article(request,aid):
    upd_cate=article.objects.get(artice_id=aid)
    if request.method=='POST':
        arti=request.POST['arti']
        details=request.POST['details']
        upd_cate.article=arti
        upd_cate.details=details
        upd_cate.save()
        # return HttpResponse("<script>alert('Successfully Updated');window.location='/managecategory'</script>")
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/photographer_manage_articles'})

    return render(request,'photographer_manage_articles.html',{'upd_cate':upd_cate})

def delete_article(request,aid):
    dele_cate=article.objects.get(artice_id=aid)
    dele_cate.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/managecategory'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/photographer_manage_articles'})

def photographer_view_bookings(request):
    
    # view=booking.objects.filter(services__studios__studio_id=request.session['user_id'])

    assignp = assignphoto.objects.filter(photographers_id=request.session['user_id'])
    # outs = booking.objects.filter(booking__in=assignp)
    # print(outs)
    return render(request,'photographer_view_bookings.html',{'view':assignp })

def photographeraddprotfolio(request):
    catview=category.objects.all()
    if request.method=='POST':
        ss=photographer.objects.get(photographer_id=request.session['user_id'])
        title=request.POST['title']
        uploaded_video=request.FILES['upload']
        fs = FileSystemStorage()
        f_nam = fs.save(uploaded_video.name, uploaded_video)
        # pu_ty=request.POST['type']
        cat=request.POST['cat']
        up_myworks=protfolio(title=title,files=f_nam,type=uploaded_video.content_type,photographers_id=request.session['user_id'],category_id=cat)
        up_myworks.save()
        return render(request,'toaster.html',{'message':'Successfully Updated','location': '/photographeraddprotfolio'})
    view1=protfolio.objects.all()
    return render(request,'photographeraddprotfolio.html',{'view1':view1,'catview':catview})

def photographer_remove_works(request,id):
    pro_del=protfolio.objects.get(protfolio_id=id)
    pro_del.delete()
    # return HttpResponse("<script>alert('Successfully Removed');window.location='/addmywork'</script>")
    return render(request,'toaster.html',{'message':'Successfully Removed','location': '/photographeraddprotfolio'})

def producer_make_chat(request,uid):
    if request.method=='POST':
        chats=request.POST['chat']
        dates=date.today()
        feed_back=chat(sender_id=request.session['login_id'],receiver_id=uid,message=chats,date=dates)
        feed_back.save()
        return render(request,'toaster.html',{'message':'Successfully Added','location': '/producer_make_chat/%s' %(uid)})
    view=chat.objects.filter(Q(sender_id=request.session['login_id'],receiver_id=uid) | Q(sender_id=uid,receiver_id=request.session['login_id']))
    return render(request,'producer_make_chat.html',{'view':view,'uid':request.session['login_id']})