from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('login',views.login_page,name='login'),
    path('user_registration',views.user_reg,name='user_registration'),
    path('public_view_category/<ids>',views.public_view_category,name='public_view_category'),
    path('forgot',views.forgot), 
    path('newpas',views.newpas),  
    path('otp',views.otp,name='otp'),

    # ////////////////////////////// Admin ///////////////////////////////////
    path('adminhome',views.admin_home,name='adminhome'),
    path('viewuser',views.admin_view_user,name='view_user'),
    path('updateusertoblock/<lid>',views.updateusertoblock,name='updateusertoblock'),
    path('updateusertounblock/<lid>',views.updateusertounblock,name='updateusertounblock'),
    path('updateusertoaccept/<lid>',views.updateusertoaccept,name='updateusertoaccept'),
    path('updateusertoreject/<lid>',views.updateusertoreject,name='updateusertoreject'),
    path('viewstudio',views.admin_view_studio,name='view_studio'),
    path('updatestudiotoblock/<lid>',views.updatestudiotoblock,name='updatestudiotoblock'),
    path('updatestudiotounblock/<lid>',views.updatestudiotounblock,name='updatestudiotounblock'),
    path('updatestudiotoaccept/<lid>',views.updatestudiotoaccept,name='updatestudiotoaccept'),
    path('updatestudiotoreject/<lid>',views.updatestudiotoreject,name='updatestudiotoreject'),
    
    
    path('viewphotographer',views.admin_view_photographer,name='view_photographer'),
    path('updatephototoblock/<lid>',views.updatephototoblock,name='updatephototoblock'),
    path('updatephototounblock/<lid>',views.updatephototounblock,name='updatephototounblock'),
    path('managecategory',views.admin_manage_category,name="managecategory"),
    path('updatecategory/<category_id>',views.update_category,name='updatecategory'),
    path('deletecategory/<category_id>',views.delete_category,name='deletecategory'),
    path('viewbookings',views.admin_view_bookings,name='viewbookings'),
    
    path('admin_view_rated/<pid>',views.admin_view_rated,name='admin_view_rated'),
    path('viewfeedback',views.admin_view_feedback,name='adminviewfeedback'),
    path('admin_view_complaints',views.admin_view_complaints,name='admin_view_complaints'),
    path('admin_send_reply/<cid>',views.admin_send_reply,name='admin_send_reply'),
    path('admin_view_report',views.admin_view_report,name='admin_view_report'),
    path('admin_view_camara_report',views.admin_view_camara_report,name='admin_view_camara_report'),
    

    
    
    
    # /////////////////////////////////// user //////////////////////////////////
    path('userhome',views.user_home,name='userhome'),
    path('userviewservice/<id>',views.user_view_service,name='userviewservice'),
    path('userbookservice/<service_id>/<amount>',views.user_book_service,name='userbookservice'),
    path('userviewbooking',views.user_view_booking,name='userviewbooking'),
    path('make_advance_payment/<booking_id>',views.make_advance_payment,name='make_advance_payment'),
    path('make_full_payment/<booking_id>',views.make_full_payment,name='make_full_payment'),
    path('viewuploadedvideo/<booking_id>',views.view_uploaded_video,name='viewuploadedvideo'),
    path('userviewwork/<id>',views.user_view_work,name='userviewwork'),
    path('user_view_category',views.user_view_category,name='user_view_category'),
    path('useraddfeedback',views.user_add_feedback,name='useraddfeedback'),
    path('updatestatustocompleted<id>',views.user_add_feedback,name='updatestatustocompleted'),
    path('userupdateprofile',views.userupdateprofile,name='userupdateprofile'),
    path('user_view_photographer',views.user_view_photographer,name='user_view_photographer'),
    path('user_assigned_photographer/<bid>',views.user_assigned_photographer,name='user_assigned_photographer'),
    path('user_view_camera',views.user_view_camera,name='user_view_camera'),
    path('user_send_request/<cid>',views.user_send_request,name='user_send_request'),
    path('user_view_request',views.user_view_request,name='user_view_request'),
    path('user_add_rating/<pid>',views.user_add_rating,name='user_add_rating'),
    path('user_add_complants',views.user_add_complants,name='user_add_complants'),
    path('user_view_protolio/<pid>/<category_id>',views.user_view_protolio,name='user_view_protolio'),
    path('user_view_potcategory/<pid>',views.user_view_potcategory,name='user_view_potcategory'),
    
    
    path('userreturncamera/<rid>',views.userreturncamera,name='userreturncamera'),
    path('user_make_chat/<pid>',views.user_make_chat,name='user_make_chat'),
    path('user_view_studio/<sid>',views.user_view_studio,name='user_view_studio'),
    
    
    
    
    
    # ////////////////////////// Public ////////////////////////
    path('publicviewservice/<category_id>',views.public_view_service,name='publicviewservice'),
    path('publicviewmyworks/<sid>',views.public_view_myworks,name='publicviewmyworks'),
    path('acceptcustomer_username/<id>',views.acceptcustomer_username),
    path('user_payment_complete/<id>/<type>/<tt>',views.user_payment_complete),
    path('rpay',views.rpay,name='rpay'),
    path('user_make_payment/<id>/<type>',views.user_make_payment,name='user_make_payment'),
    path('public_view_studios/<sid>',views.public_view_studios,name='public_view_studios'),
    

    # ///////////////////////// Studio /////////////////////////////
    path('studiohome',views.studio_home,name='studiohome'),
    path('studio_update_profile',views.studio_update_profile,name='studio_update_profile'),
    path('studio_manage_photographer',views.studio_manage_photographer,name='studio_manage_photographer'),
    path('studiodeletephotographer/<lid>',views.studiodeletephotographer,name='studiodeletephotographer'),
    path('studio_manage_camera',views.studio_manage_camera,name='studio_manage_camera'),
    path('studioupdatecamera/<cid>',views.studioupdatecamera,name='studioupdatecamera'),
    path('studiodeletecamera/<cid>',views.studiodeletecamera,name='studiodeletecamera'),
    path('studionotavilablecamera/<cid>',views.studionotavilablecamera,name='studionotavilablecamera'),
    path('studioavilablecamera/<cid>',views.studioavilablecamera,name='studioavilablecamera'),
    path('studio_manage_service',views.studio_manage_service,name='studio_manage_service'),
    path('updateservice/<service_id>',views.update_service,name='updateservice'),
    path('deleteservice/<service_id>',views.delete_service,name='deleteservice'),
    path('studio_add_myworks',views.studio_add_myworks,name='studio_add_myworks'),
    path('studio_remove_works/<id>',views.studio_remove_works,name='studio_remove_works'),
    path('studio_view_bookings',views.studio_view_bookings,name='studio_view_bookings'),
    path('studio_view_photographers/<booking_id>/<bookingfordate>',views.studio_view_photographers,name='studio_view_photographers'),
    path('studio_accept_booking/<pid>/<bid>/<bdate>',views.studio_accept_booking,name='studio_accept_booking'),
    path('studio_reject_booking/<booking_id>',views.studio_reject_booking,name='studio_reject_booking'),
    
    path('studio_view_advance_payment/<booking_id>',views.studio_view_advance_payment,name='studio_view_advance_payment'),
    path('studio_update_booking_status/<booking_id>',views.studio_update_booking_status,name='studio_update_booking_status'),
    path('studio_upload_video/<booking_id>',views.studio_upload_video,name='studio_upload_video'),
    path('studio_view_request',views.studio_view_request,name='studio_view_request'),
    path('studio_accept_request/<rid>',views.studio_accept_request,name='studio_accept_request'),
    path('studio_reject_request/<rid>',views.studio_reject_request,name='studio_reject_request'),
    path('studio_view_rated/<pid>',views.studio_view_rated,name='studio_view_rated'),
    path('studio_payed_offline/<bid>',views.studio_payed_offline,name='studio_payed_offline'),
    path('studio_view_booking_report',views.studio_view_booking_report,name='studio_view_booking_report'),
    path('studio_view_camara_report',views.studio_view_camara_report,name='studio_view_camara_report'),
    


    


    # /////////////////////////// Photographer ///////////////////////
    path('photographerhome',views.photgrapher_home,name='photgrapher_home'),
    path('photographer_update_profile',views.photographer_update_profile,name='photographer_update_profile'),
    path('photographer_manage_articles',views.photographer_manage_articles,name='photographer_manage_articles'),
    path('update_article/<aid>',views.update_article,name='update_article'),
    path('delete_article/<aid>',views.delete_article,name='delete_article'),
    path('photographer_view_bookings',views.photographer_view_bookings,name='photographer_view_bookings'),
    path('photographeraddprotfolio',views.photographeraddprotfolio,name='photographeraddprotfolio'),
    path('photographer_remove_works/<id>',views.photographer_remove_works,name='photographer_remove_works'),
    path('producer_make_chat/<uid>',views.producer_make_chat,name='producer_make_chat'),

    


    

]
