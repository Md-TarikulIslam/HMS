from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from crudd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('employee/', views.Viewemployees, name='employee'),
    path('patient/', views.Viewpatient, name='patient'),
    path('contact/', views.viewContact, name="contact"),
    path('message_me/', views.message_meView, name="message_me"),
    path('doctor/', views.Viewdoctor, name='doctor'),
    path('salary/', views.Viewsalary, name='salary'),
    path('medicine/', views.Viewmedicine, name='medicine'),
    path('opd/', views.Viewopd, name='opd'),
    path('ipd/', views.Viewipd, name='ipd'),
    path('ot/', views.Viewot, name='ot'),
    path('bed/', views.Viewbed, name='bed'),
    path('members/',include('django.contrib.auth.urls') ),
    path('members/', include('members.urls')),


    path("insert_data", views.insert_data,  name="insert_data"),
    path("update_data<int:id>", views.update_data,  name="update_data"),
    path("delete_data<int:id>", views.delete_data,  name="delete_data"),

    path("ins_data", views.ins_data,  name="ins_data"),
    path("upd_data<int:id>", views.upd_data,  name="upd_data"),
    path("del_data<int:id>", views.del_data,  name="del_data"),

    path("in_data", views.in_data,  name="in_data"),
    path("up_data<int:id>", views.up_data,  name="up_data"),
    path("de_data<int:id>", views.de_data,  name="de_data"),

    path("n_data", views.n_data,  name="n_data"),
    path("p_data<int:id>", views.p_data,  name="p_data"),
    path("e_data<int:id>", views.e_data,  name="e_data"),

    
    path("give_data", views.give_data,  name="give_data"),
    path("ed_data<int:id>", views.ed_data,  name="ed_data"),
    path("erase_data<int:id>", views.erase_data,  name="erase_data"),

    path("inser_data", views.inser_data,  name="inser_data"),
    path("upda_data<int:id>", views.upda_data,  name="upda_data"),
    path("delet_data<int:id>", views.delet_data,  name="delet_data"),

    path("inse_data", views.inse_data,  name="inse_data"),
    path("updat_data<int:id>", views.updat_data,  name="updat_data"),
    path("dele_data<int:id>", views.dele_data,  name="dele_data"),

    path("inot", views.inot,  name="inot"),
    path("upot<int:id>", views.upot,  name="upot"),
    path("deot<int:id>", views.deot,  name="deot"),

    path("inb", views.inb,  name="inb"),
    path("upb<int:id>", views.upb,  name="upb"),
    path("deb<int:id>", views.deb,  name="deb"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "HMS Login"  
admin.site.site_title  =  "HMS's Admin Site"
admin.site.index_title  =  "Hospital Management System"