from django.db import models

# Create your models here.

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)
    
class studio(models.Model):
    studio_id=models.AutoField(primary_key=True)
    logins=models.ForeignKey(login,on_delete=models.CASCADE)
    studioname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    since=models.CharField(max_length=225)
    licence=models.CharField(max_length=225)
    
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    logins=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.EmailField()

class photographer(models.Model):
    photographer_id=models.AutoField(primary_key=True)
    studios=models.ForeignKey(studio,on_delete=models.CASCADE)
    logins=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    pincode=models.CharField(max_length=7)
    phone=models.CharField(max_length=225)
    email=models.EmailField()

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=225)
    image=models.CharField(max_length=225)
   
    
class service(models.Model):
    service_id=models.AutoField(primary_key=True)
    categorys=models.ForeignKey(category,on_delete=models.CASCADE)
    studios=models.ForeignKey(studio,on_delete=models.CASCADE)
    service=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)
    details=models.CharField(max_length=225)
    image=models.CharField(max_length=1000)
    
class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    services=models.ForeignKey(service,on_delete=models.CASCADE)
    users=models.ForeignKey(user,on_delete=models.CASCADE)
    venue=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    bookingfordate=models.CharField(max_length=225)
    time=models.CharField(max_length=225)
    amounts=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    pref=models.CharField(max_length=225)
    photographers=models.ForeignKey(photographer,on_delete=models.CASCADE)

class assignphoto(models.Model):
    assignphoto_id=models.AutoField(primary_key=True)
    bookings=models.ForeignKey(booking,on_delete=models.CASCADE)
    photographers=models.ForeignKey(photographer,on_delete=models.CASCADE)
    
    
class payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    bookings=models.ForeignKey(booking,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class uploads(models.Model):
    upload_id=models.AutoField(primary_key=True)
    bookingss=models.ForeignKey(booking,on_delete=models.CASCADE)
    file=models.FileField()
    type=models.CharField(max_length=255)
    link=models.CharField(max_length=255)
    
class mywork(models.Model):
    mywork_id=models.AutoField(primary_key=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    studios=models.ForeignKey(studio,on_delete=models.CASCADE)
    works=models.CharField(max_length=255)
    files=models.FileField()
    type=models.CharField(max_length=255)
    
class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    users=models.ForeignKey(user,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255)
    date=models.CharField(max_length=255)

class article(models.Model):
    artice_id=models.AutoField(primary_key=True)
    photographers=models.ForeignKey(photographer,on_delete=models.CASCADE)
    article=models.CharField(max_length=255)
    details=models.CharField(max_length=255)
    date=models.CharField(max_length=255)

class chat(models.Model):
    artice_id=models.AutoField(primary_key=True)
    sender_id=models.IntegerField(max_length=11)
    receiver_id=models.IntegerField(max_length=11)
    message=models.CharField(max_length=255)
    date=models.CharField(max_length=255)

class camera(models.Model):
    camera_id=models.AutoField(primary_key=True)
    studios=models.ForeignKey(studio,on_delete=models.CASCADE)
    camera=models.CharField(max_length=255)
    resolution=models.CharField(max_length=255)
    sensortypeandsize=models.CharField(max_length=255)
    lensetype=models.CharField(max_length=255)
    connectiontype=models.CharField(max_length=255)
    amountperday=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    cam_img=models.CharField(max_length=255)
    
    
class requests(models.Model):
    request_id=models.AutoField(primary_key=True)
    users=models.ForeignKey(user,on_delete=models.CASCADE)
    cameras=models.ForeignKey(camera,on_delete=models.CASCADE)
    date=models.CharField(max_length=255)
    requestedfor=models.CharField(max_length=255)  
    status=models.CharField(max_length=255)  

class review(models.Model):
    review_id=models.AutoField(primary_key=True)
    users=models.ForeignKey(user,on_delete=models.CASCADE)
    photographers=models.ForeignKey(photographer,on_delete=models.CASCADE)
    rate=models.CharField(max_length=255)
    review=models.CharField(max_length=255)
    date=models.CharField(max_length=255)

class complaints(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    users=models.ForeignKey(user,on_delete=models.CASCADE)
    complaints=models.CharField(max_length=255)
    reply=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    
class protfolio(models.Model):
    protfolio_id=models.AutoField(primary_key=True)
    photographers=models.ForeignKey(photographer,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    files=models.FileField()
    type=models.CharField(max_length=255)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    