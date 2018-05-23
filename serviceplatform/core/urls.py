# encoding:utf-8

from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^index/$', views.index, name="index"),
    url(r'^logout/$', views.logout, name="logout"),

    url(r'^company_view_list/$', views.company_view_list, name="company_view_list"),
    url(r'^create_new_company/$', views.create_new_company, name="create_new_company"),  # create company
    url(r'^company_detail/(?P<company_id>[0-9]+)$', views.company_detail, name="company_detail"),  # company detail
    url(r'^edit_company/$', views.edit_company, name="edit_company"),  # edit company
    url(r'^delete_single_company/$', views.delete_single_company, name="delete_single_company"),  # delete company

    url(r'^person_view_list/$', views.person_view_list, name="person_view_list"),
    url(r'^create_new_person/$', views.create_new_person, name="create_new_person"),  # create person
    url(r'^person_detail/(?P<person_id>[0-9]+)$', views.person_detail, name="person_detail"),
    url(r'^edit_person/$', views.edit_person, name="edit_person"),  # edit person
    url(r'^delete_single_person/$', views.delete_single_person, name="delete_single_person"),  # delete person

    url(r'^device_view_list/$', views.device_view_list, name="device_view_list"),
    url(r'^create_new_device/$', views.create_new_device, name="create_new_device"),  # create device
    url(r'^device_detail/(?P<device_id>[0-9]+)$', views.device_detail, name="device_detail"),
    url(r'^edit_device/$', views.edit_device, name="edit_device"),

    url(r'^sign/$', views.sign, name="sign"),  # interface sign
    url(r'^check_create_company_name/$', views.check_create_company_name, name="check_create_company_name"),  # check
    url(r'^check_edit_company_name/$', views.check_edit_company_name, name="check_edit_company_name"),  # check edit company
    url(r'^check_create_company_number/$', views.check_create_company_number, name="check_create_company_number"),
    url(r'^check_edit_company_number/$', views.check_edit_company_number, name="check_edit_company_number"),  # check edit company

    url(r'^check_create_person_id_card/$', views.check_create_person_id_card, name="check_create_person_id_card"),
    url(r'^check_create_person_social/$', views.check_create_person_social, name="check_create_person_social"),
    url(r'^check_create_person_unemployment/$', views.check_create_person_unemployment, name="check_create_person_unemployment"),

    url(r'^check_edit_person_id_card/$', views.check_edit_person_id_card, name="check_edit_person_id_card"),
    url(r'^check_edit_person_social/$', views.check_edit_person_social, name="check_edit_person_social"),
    url(r'^check_edit_person_unemployment/$', views.check_edit_person_unemployment, name="check_edit_person_unemployment"),

    url(r'^check_create_device_number/$', views.check_create_device_number, name="check_create_device_number"),
    url(r'^check_edit_device_number/$', views.check_edit_device_number, name="check_edit_device_number"),


]