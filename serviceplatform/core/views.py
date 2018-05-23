from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from PIL import Image,ImageDraw,ImageFont
from math import ceil
import random
import os
import sys
import io as cStringIO
from datetime import datetime,timedelta
import hashlib
from django.core.files.storage import default_storage
import json
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import *
from django.db import connection
from django.utils import timezone
try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.
from django.utils.decorators import available_attrs
from django.contrib.auth import authenticate, logout as user_logout, login as user_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.views.decorators.http import require_http_methods
import urllib.parse
import urllib.request
import base64
from core.models import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from core.serializers import *
from core.common import *
from django.conf import settings
import simplejson


def login(req):
    if req.method == 'GET':
        if req.user.is_authenticated:
            return HttpResponseRedirect('/index')
        return render(req, 'login/login.html',locals())
    else:
        r = {}
        args = req.POST
        username = args.get('username')
        pwd = args.get('pwd')
        user = authenticate(username=username, password=pwd)
        if user:
            user_login(req, user)
            r['status'] = '200'
            r['message'] = '成功登录'
            return HttpResponse(json.dumps(r, ensure_ascii=False))
        else:
            r['status'] = '403'
            r['message'] = '用户名或者密码错误，或者用户已经被禁用。'
            return HttpResponse(json.dumps(r, ensure_ascii=False))


@csrf_exempt
def logout(req):
    req.session.clear()
    user_logout(req)
    # raise Http404("Question does not exist")
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def index(req):
    return render(req, "web/index.html", locals())


def has_perm():  # has perms to use interface
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            r = {'status': '500'}
            try:
                request = json.loads(request.body.decode('utf-8'))
                device_id = request['deviceId']
                key = request['key']
                if key == settings.SECRET_KEY and device_id:
                    u = Device.objects.filter(key=device_id)
                    if u:
                        return func(request, *args, **kwargs)
                    else:
                        return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
            except Exception as e:
                return HttpResponse(json.dumps(r, ensure_ascii=False))
        return inner
    return decorator


# face & finger interface
@csrf_exempt
@has_perm()
def sign(req):
    r = {'status': 0}
    try:
        # if req.method == "POST":
            # req = json.loads(req.body.decode('utf-8'))
        card_info = req["cardinfo"]
        face = req["face"]
        finger = req["finger"]
        device_id = req["deviceId"]
        if card_info and face and finger:
            id_card = card_info.get("idcard")
            person = Person.objects.filter(id_card=id_card)
            device = Device.objects.filter(key=device_id)
            if person and device:
                person[0].name = card_info["name"]
                person[0].gender = card_info["sex"]
                person[0].address = card_info["address"]
                person[0].birthday = stringtoDate(card_info["birthday"])
                person[0].nation = card_info["nation"]
                person[0].org = card_info["org"]
                person[0].card_start_date = card_info["startdate"]
                person[0].card_end_date = card_info["enddate"]
                person[0].head_image = card_info["headimage"]
                person[0].save()

                # device[0].number = device_id
                # device[0].address = req["deviceAdd"]
                # device[0].save()

                sign = Sign()
                sign.person = person[0]
                sign.add_time = req["addtime"]
                sign.add_date = req["adddate"]
                sign.serviceType = req["serviceType"]
                sign.device = device[0]
                sign.scene_image = face["sceneimage"]
                sign.face_score = face["faceScore"]
                sign.face_result = face["faceResult"]
                sign.finger_data = finger["FingerData"]
                sign.fp_score = finger["fpScore"]
                sign.fp_result = finger["fpResult"]
                sign.save()
                r["status"] = 1
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                return HttpResponse(json.dumps(r, ensure_ascii=False))
        else:
            return HttpResponse(json.dumps(r, ensure_ascii=False))
        # return HttpResponse(json.dumps(r, ensure_ascii=False))

    except Exception as e:
        return HttpResponse(json.dumps(r, ensure_ascii=False))


# device
@login_required(login_url='/')
def device_view_list(req):
    device = Device.objects.all()
    return render(req, "web/device/device_view.html", locals())


@login_required(login_url='/')
def create_new_device(req):
    if req.method == 'GET':
        return render(req, "web/device/device_add.html", locals())

    if req.method == 'POST':
        r = {'status': '500'}
        try:
            address = req.POST.get("address", "")
            device_number = req.POST.get("device_number", "")
            active = req.POST.get("active", "")

            device = Device()
            if not address:
                r['msg'] = '创建设备信息时发生错误，必须填写设备地址。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                device.address = address

            if device_number:
                if Device.objects.filter(number=device_number):
                    r['msg'] = '创建设备信息时发生错误，设备编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    device.number = device_number
                    md5 = generate_md5(device_number+"john")
                    device.key = md5
            else:
                r['msg'] = '创建设备信息时发生错误，必须填写设备编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            device.active = active
            device.save()
            # raise Exception("抛出一个异常")
            r['status'] = '200'
            r['msg'] = '成功创建设备信息！'
            r['device_id'] = str(device.id)

            return HttpResponse(json.dumps(r, ensure_ascii=False))

        except Exception as e:
            r['msg'] = '创建设备信息时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
            return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def edit_device(req):
    if req.method == 'GET':
        device_id = req.GET.get('device_id', None)
        device = Device.objects.get(id=device_id)
        return render(req, "web/device/device_edit.html", locals())

    if req.method == 'POST':
        r = {'status': '500'}
        try:
            address = req.POST.get("address", "")
            device_number = req.POST.get("device_number", "")
            active = req.POST.get("active", "")
            device_id = req.POST.get("device_id", None)
            device = Device()
            if not address:
                r['msg'] = '编辑设备信息时发生错误，必须填写设备地址。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                device.address = address

            if device_number:
                if Device.objects.filter(Q(number=device_number), ~Q(id=device_id)):
                    r['msg'] = '编辑设备信息时发生错误，设备编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    device.number = device_number
                    md5 = generate_md5(device_number+"john")
                    device.key = md5
            else:
                r['msg'] = '编辑设备信息时发生错误，必须填写设备编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            device.active = active
            device.save()
            # raise Exception("抛出一个异常")
            r['status'] = '200'
            r['msg'] = '成功编辑设备信息！'
            r['device_id'] = str(device.id)

            return HttpResponse(json.dumps(r, ensure_ascii=False))

        except Exception as e:
            r['msg'] = '编辑设备信息时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
            return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def device_detail(req, device_id):
    device = Device.objects.filter(id=device_id)[0]
    return render(req, "web/device/device_detail.html", locals())


# company
@csrf_exempt
@login_required(login_url='/')
def create_new_company(req):
    if req.method == 'GET':
        action_type = 'create'
        bank = Bank.objects.all()
        policy = PolicyTypes.objects.all()
        return render(req, "web/company/company_add.html", locals())

    if req.method == 'POST':
        r = {}
        try:
            name = req.POST.get("name", "")
            company_phone = req.POST.get("company_phone", "")
            contract_phone = req.POST.get("contract_phone", "")
            contract_people = req.POST.get("contract_people", "")
            company_num = req.POST.get("company_num", "")
            policy_types = req.POST.get("policy_types", "")
            general_bank = req.POST.get("general_bank", "")
            bank_branch = req.POST.get("bank_branch", "")
            account_name = req.POST.get("account_name", "")
            bank_account = req.POST.get("bank_account", "")
            logout = req.POST.get("logout", "")
            remark = req.POST.get("remark", "")

            company = Company()
            if name:
                if Company.objects.filter(name=name):
                    r['status'] = '500'
                    r['msg'] = '创建单位时发生错误，单位名称重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    company.name = name
            company.tel = company_phone

            company.contract_tel = contract_phone
            company.contract_people = contract_people
            if company_num:
                if Company.objects.filter(company_num=company_num):
                    r['status'] = '500'
                    r['msg'] = '创建单位时发生错误，单位编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    company.company_num = company_num
            if policy_types:
                company.policy_types = PolicyTypes.objects.get(id=policy_types)
            company.general_bank = Bank.objects.get(id=general_bank)
            company.bank_branch = bank_branch
            company.account_name = account_name
            company.bank_account = bank_account
            company.logout = logout
            company.remark = remark
            company.save()
            # raise Exception("抛出一个异常")
            r['status'] = '200'
            r['msg'] = '成功创建单位！'
            r['company_id'] = str(company.id)
            return HttpResponse(json.dumps(r, ensure_ascii=False))

        except Exception as e:
            r['msg'] = '创建单位时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
            r['status'] = '500'
            return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def company_detail(req, company_id):
    company = Company.objects.filter(id=company_id)[0]
    return render(req, "web/company/company_detail.html", locals())


@login_required(login_url='/')
def company_view_list(req):
    company = Company.objects.all()
    return render(req, "web/company/company_view.html", locals())


@login_required(login_url='/')
def edit_company(req):
    try:
        if req.method == 'GET':
            company_id = req.GET.get('company_id', None)
            company = Company.objects.get(id=company_id)
            bank = Bank.objects.all()
            policy = PolicyTypes.objects.all()
            return render(req, "web/company/company_edit.html", locals())
    except Exception as e:
        company = Company.objects.all()
        return render(req, "web/company/company_view.html", locals())

    try:
        if req.method == 'POST':
            r = {}
            company_id = req.POST.get("company_id", "")
            name = req.POST.get("name", "")
            company_phone = req.POST.get("company_phone", "")
            contract_phone = req.POST.get("contract_phone", "")
            contract_people = req.POST.get("contract_people", "")
            company_num = req.POST.get("company_num", "")
            policy_types = req.POST.get("policy_types", "")
            general_bank = req.POST.get("general_bank", "")
            bank_branch = req.POST.get("bank_branch", "")
            account_name = req.POST.get("account_name", "")
            bank_account = req.POST.get("bank_account", "")
            logout = req.POST.get("logout", "")
            remark = req.POST.get("remark", "")
            company = Company.objects.filter(id=company_id)[0]
            if name:
                if Company.objects.filter(Q(name=name), ~Q(id=company.id)):

                    r['status'] = '500'
                    r['msg'] = '编辑单位时发生错误，单位名称重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    company.name = name
            company.tel = company_phone
            company.contract_tel = contract_phone
            company.contract_people = contract_people
            if company_num:
                if Company.objects.filter(Q(company_num=company_num), ~Q(id=company.id)):
                    r['status'] = '500'
                    r['msg'] = '编辑单位时发生错误，单位编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    company.company_num = company_num
            if policy_types:
                company.policy_types = PolicyTypes.objects.get(id=policy_types)
            company.general_bank = Bank.objects.get(id=general_bank)
            company.bank_branch = bank_branch
            company.account_name = account_name
            company.bank_account = bank_account
            company.logout = logout
            company.remark = remark
            company.save()

            r['status'] = '200'
            r['msg'] = '成功编辑单位！'
            r['company_id'] = str(company.id)
            return HttpResponse(json.dumps(r, ensure_ascii=False))

    except Exception as e:
        r = {}
        r['msg'] = '编辑单位时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
        r['status'] = '500'
        return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def delete_company(req):
    r = {}
    try:
        post_args = req.POST
        company = Company.objects.filter(id__in=post_args.getlist('ids[]'))
        # r['msg'] = '%s deleted.' % (",".join([x.title for x in company]))
        if not company:
            r['status'] = '400'
            return HttpResponse(json.dumps(r, ensure_ascii=False))
        for x in company:
            company.delete()
        r['status'] = '200'
        return HttpResponse(json.dumps(r, ensure_ascii=False))
    except Exception as e:
        r['msg'] = '删除单位失败!'
        r['status'] = '500'
        return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def delete_single_company(req):
    r = {}
    try:
        post_args = req.POST
        company = Company.objects.filter(id=post_args.get('id'))
        # r['msg'] = '%s deleted.' % (",".join([x.title for x in company]))
        if not company:
            r['status'] = '404'
            return HttpResponse(json.dumps(r, ensure_ascii=False))
        for x in company:
            company.delete()
        r['status'] = '200'
        return HttpResponse(json.dumps(r, ensure_ascii=False))

    except Exception as e:
        r['msg'] = '删除单位失败!'
        r['status'] = '500'
        return HttpResponse(json.dumps(r, ensure_ascii=False))


# person
@login_required(login_url='/')
def person_view_list(req):
    person = Person.objects.all()
    return render(req, "web/person/person_view.html", locals())


@csrf_exempt
@login_required(login_url='/')
def create_new_person(req):
    if req.method == 'GET':
        return render(req, "web/person/person_add.html", locals())

    if req.method == 'POST':
        r = {'status': '500'}
        try:
            name = req.POST.get("name", "")
            nation = req.POST.get("nation", "")
            social = req.POST.get("social", "")
            idcard = req.POST.get("idcard", "")
            unemployment = req.POST.get("unemployment", "")
            address = req.POST.get("address", "")
            active = req.POST.get("active", "")
            remark = req.POST.get("remark", "")
            tel = req.POST.get("tel", "")

            person = Person()
            if not name:
                r['msg'] = '必须填写姓名。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                person.name = name
            person.tel = tel
            if social:
                if Person.objects.filter(social_security_number=social):
                    r['msg'] = '创建失业人员时发生错误，社保编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    person.social_security_number = social
            else:
                r['msg'] = '必须填写社保编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))

            if idcard:
                if Person.objects.filter(id_card=idcard):
                    r['msg'] = '创建失业人员时发生错误，身份证号码重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    if check_id_card(idcard):
                        sex = int(idcard[16])
                        person.gender = "female" if sex % 2 == 0 else "male"
                        person.birthday = stringtoDate(idcard[6:10] + "-" + idcard[10:12] + "-" + idcard[12:14])
                        person.id_card = idcard
                    else:
                        r['msg'] = '创建失业人员时发生错误，身份证号码格式不正确。'
                        return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                r['msg'] = '必须填写身份证号码。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))

            if unemployment:
                if Person.objects.filter(unemployment_number=unemployment):
                    r['msg'] = '创建失业人员时发生错误，失业登记证编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    person.unemployment_number = unemployment
            else:
                r['msg'] = '必须填写失业登记证编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            person.nation = nation
            person.address = address
            person.remark = remark
            person.active = active
            person.save()
            r['status'] = '200'
            r['msg'] = '成功创建单位！'
            r['person_id'] = str(person.id)
            return HttpResponse(json.dumps(r, ensure_ascii=False))

        except Exception as e:
            r['msg'] = '创建单位时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
            return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def person_detail(req, person_id):
    person = Person.objects.filter(id=person_id)[0]
    return render(req, "web/person/person_detail.html", locals())


@login_required(login_url='/')
def edit_person(req):
    r = {}
    try:
        if req.method == 'GET':
            person_id = req.GET.get('person_id', None)
            person = Person.objects.get(id=person_id)
            return render(req, "web/person/person_edit.html", locals())
    except Exception as e:
        person = Person.objects.all()
        return render(req, "web/person/person_view.html", locals())

    try:
        if req.method == 'POST':
            r = {'status': '500'}
            person_id = req.POST.get("person_id", None)
            name = req.POST.get("name", "")
            nation = req.POST.get("nation", "")
            social = req.POST.get("social", "")
            idcard = req.POST.get("idcard", "")
            unemployment = req.POST.get("unemployment", "")
            address = req.POST.get("address", "")
            active = req.POST.get("active", "")
            remark = req.POST.get("remark", "")
            tel = req.POST.get("tel", "")

            person = Person.objects.filter(id=person_id)[0]
            if name:
                person.name = name
            else:
                r['msg'] = '编辑失业人员时发生错误，必须填写姓名。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            person.tel = tel
            person.nation = nation
            person.address = address
            person.remark = remark
            person.active = active
            if social:
                if Person.objects.filter(Q(social_security_number=social), ~Q(id=person_id)):
                    r['msg'] = '编辑失业人员时发生错误，社保编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    person.social_security_number = social
            else:
                r['msg'] = '必须填写社保编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))

            if idcard:
                if Person.objects.filter(Q(id_card=idcard), ~Q(id=person_id)):
                    r['msg'] = '编辑失业人员时发生错误，身份证号码重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    if check_id_card(idcard):
                        sex = int(idcard[16])
                        person.gender = "female" if sex % 2 == 0 else "male"
                        person.birthday = stringtoDate(idcard[6:10] + "-" + idcard[10:12] + "-" + idcard[12:14])
                        person.id_card = idcard
                    else:
                        r['msg'] = '编辑失业人员时发生错误，身份证号码格式不正确。'
                        return HttpResponse(json.dumps(r, ensure_ascii=False))
            else:
                r['msg'] = '必须填写身份证号码。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))

            if unemployment:
                if Person.objects.filter(Q(unemployment_number=unemployment), ~Q(id=person_id)):
                    r['msg'] = '创建失业人员时发生错误，失业登记证编号重复。'
                    return HttpResponse(json.dumps(r, ensure_ascii=False))
                else:
                    person.unemployment_number = unemployment
            else:
                r['msg'] = '必须填写失业登记证编号。'
                return HttpResponse(json.dumps(r, ensure_ascii=False))
            person.save()

            r['status'] = '200'
            r['msg'] = '成功编辑单位！'
            r['person_id'] = str(person.id)
            return HttpResponse(json.dumps(r, ensure_ascii=False))

    except Exception as e:
        r['msg'] = '编辑失业人员时发生错误，请检查输入的字段格式是否正确，或及时与管理员联系。谢谢！'
        return HttpResponse(json.dumps(r, ensure_ascii=False))


@login_required(login_url='/')
def delete_single_person(req):
    r = {}
    try:
        post_args = req.POST
        person = Person.objects.filter(id=post_args.get('id'))
        if not person:
            r['status'] = '404'
            return HttpResponse(json.dumps(r, ensure_ascii=False))
        for x in person:
            person.delete()
        r['status'] = '200'
        return HttpResponse(json.dumps(r, ensure_ascii=False))

    except Exception as e:
        r['msg'] = '删除单位失败!'
        r['status'] = '500'
        return HttpResponse(json.dumps(r, ensure_ascii=False))


# check function
@login_required(login_url='/')
def check_create_company_name(req):
    if req.method == "POST":
        value = req.POST.get("company_name", None)
        if value:
            company = Company.objects.filter(name=value)
            if company:
                return HttpResponse("false")
            else:
                return HttpResponse("true")


@login_required(login_url='/')
def check_create_company_number(req):
    if req.method == "POST":
        value = req.POST.get("company_number", None)
        if value:
            company = Company.objects.filter(company_num=value)
            if company:
                return HttpResponse("false")
            else:
                return HttpResponse("true")


@login_required(login_url='/')
def check_edit_company_number(req):
    if req.method == "POST":
        value = req.POST.get("company_number", None)
        company_id = req.POST.get("company_id", None)
        if value and company_id:
            company = Company.objects.filter(Q(company_num=value), ~Q(id=company_id))
            if company:
                return HttpResponse("false")
            else:
                return HttpResponse("true")


@login_required(login_url='/')
def check_edit_company_name(req):
    if req.method == "POST":
        value = req.POST.get("company_name", None)
        company_id = req.POST.get("company_id", None)
        if value and company_id:
            company = Company.objects.filter(Q(name=value), ~Q(id=company_id))
            if company:
                return HttpResponse("false")
            else:
                return HttpResponse("true")


@login_required(login_url='/')
def check_create_person_id_card(req):
    if req.method == "POST":
        value = req.POST.get("idcard", None)
        if value:
            if Person.objects.filter(id_card=value):
                return HttpResponse("false")
            else:
                result = check_id_card(value)
                return HttpResponse("true") if result else HttpResponse("false")
    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_create_person_social(req):
    if req.method == "POST":
        value = req.POST.get("social", None)
        if value:
            return HttpResponse("false") if Person.objects.filter(social_security_number=value) else HttpResponse("true")

    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_create_person_unemployment(req):
    if req.method == "POST":
        value = req.POST.get("unemployment", None)
        if value:
            return HttpResponse("false") if Person.objects.filter(unemployment_number=value) else HttpResponse("true")

    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_edit_person_id_card(req):
    if req.method == "POST":
        value = req.POST.get("idcard", None)
        person_id = req.POST.get("person_id", None)
        if value:
            if Person.objects.filter(Q(id_card=value), ~Q(id=person_id)):
                return HttpResponse("false")
            else:
                result = check_id_card(value)
                return HttpResponse("true") if result else HttpResponse("false")
    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_edit_person_social(req):
    if req.method == "POST":
        value = req.POST.get("social", None)
        person_id = req.POST.get("person_id", None)
        if value:
            return HttpResponse("false") if Person.objects.filter(Q(social_security_number=value), ~Q(id=person_id)) else HttpResponse("true")

    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_edit_person_unemployment(req):
    if req.method == "POST":
        value = req.POST.get("unemployment", None)
        person_id = req.POST.get("person_id", None)
        if value:
            return HttpResponse("false") if Person.objects.filter(Q(unemployment_number=value), ~Q(id=person_id)) else HttpResponse("true")

    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_create_device_number(req):
    if req.method == "POST":
        value = req.POST.get("device_number", None)
        if value:
            return HttpResponse("false") if Device.objects.filter(number=value) else HttpResponse("true")
    else:
        return HttpResponse("false")


@login_required(login_url='/')
def check_edit_device_number(req):
    if req.method == "POST":
        value = req.POST.get("device_number", None)
        device_id = req.POST.get("device_id", None)
        if value:
            return HttpResponse("false") if Device.objects.filter(Q(number=value), ~Q(id=device_id)) else HttpResponse("true")
    else:
        return HttpResponse("false")