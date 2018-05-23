# encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


class PolicyTypes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)


class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tel = models.CharField(max_length=255, default="")
    company_num = models.CharField(max_length=255, default="")
    contract_people = models.CharField(max_length=255, default="")
    contract_tel = models.CharField(max_length=255, default="")
    policy_types = models.ForeignKey(PolicyTypes, null=True, blank=True, on_delete=models.CASCADE)  # 政策类型
    general_bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.CASCADE)
    bank_branch = models.CharField(max_length=255, default="")
    bank_account = models.CharField(max_length=255, default="")  # 银行账号
    account_name = models.CharField(max_length=255, default="")  # 开户名称
    remark = models.TextField(max_length=255, default="")
    logout = models.BooleanField(default=False)
    create_user = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    create_organization = models.CharField(max_length=255, default="")


class User(AbstractUser):
    name = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=255, default="")
    # company_id = models.ForeignKey(Company)
    birthday = models.DateTimeField(blank=True, null=True)


class Person(models.Model):  # person information
    name = models.CharField(max_length=255, default="")
    id_card = models.CharField(max_length=255, default="", unique=True)
    gender = models.CharField(max_length=255, default="")
    nation = models.CharField(max_length=255, default="")
    birthday = models.DateField(blank=True, null=True)
    org = models.CharField(max_length=255, default="")  # id card org
    card_start_date = models.CharField(max_length=255, default="")
    card_end_date = models.CharField(max_length=255, default="")
    head_image = models.CharField(max_length=255, default="")
    address = models.TextField(max_length=255, default="")
    social_security_number = models.CharField(max_length=255, default="")
    unemployment_number = models.CharField(max_length=255, default="")
    graduation = models.CharField(max_length=255, default="")  # 毕业时间
    tel = models.CharField(max_length=255, default="")
    remark = models.TextField(max_length=255, default="")
    active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    address = models.CharField(max_length=255, default="")
    number = models.CharField(max_length=255, default="")  # unique device number
    key = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)


class Sign(models.Model):
    person = models.ForeignKey(Person, default="")   # person
    serviceType = models.CharField(max_length=255, default="")
    add_time = models.CharField(max_length=255, default="")
    add_date = models.CharField(max_length=255, default="")
    device = models.ForeignKey(Device, blank=True, null=True)   # device
    finger_data = models.TextField(max_length=255, default="")  # finger
    fp_score = models.FloatField(default=0)
    fp_result = models.CharField(max_length=255, default="")
    scene_image = models.TextField(max_length=255, default="")  # face
    face_score = models.FloatField(default=0)
    face_result = models.CharField(max_length=255, default="")

