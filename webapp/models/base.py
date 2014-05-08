#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from motorengine import Document, IntField, DateTimeField, ListField
from motorengine import StringField, BooleanField, FloatField, JsonField
from motorengine import EmbeddedDocumentField, ReferenceField, EmailField
from motorengine.fields.base_field import BaseField
from ipaddress import IPv4Address

class IPAddrField(BaseField):
    def validate(self, value):
        try:
            i = IPv4Address(value)
            return True
        except:
            return False

class User(Document):
    email = EmailField(required=True)
    active = BooleanField(required=True, default=False)
    roles = ListField(StringField(max_length=64))
    group = JsonField()


class Game(Document):
    name = StringField(required=True, unique=True, max_length=255)
    cname = StringField(required=True, max_length=255)
    gametype = StringField(required=True, max_length=64)
    managers = ListField(ReferenceField(reference_document_type=User))
    active = BooleanField(required=True, default=True)
    online = DateTimeField(required=True, auto_now_on_insert=True)
    update = DateTimeField(required=True, auto_now_on_insert=True, 
                           auto_now_on_update=True)
    offline = DateTimeField()
    note = StringField(max_length=255)

class App(Document):
    name = StringField(required=True, unique=True, max_length=255)
    cname = StringField(required=True, max_length=255)
    game = ReferenceField(reference_document_type=Game)
    active = BooleanField(required=True, default=True)
    online = DateTimeField(required=True, auto_now_on_insert=True)
    update = DateTimeField(required=True, auto_now_on_insert=True, 
                           auto_now_on_update=True)
    offline = DateTimeField()
    note = StringField(max_length=255)

class Idc(Document):
    name = StringField(required=True, unique=True, max_length=255)
    location = StringField(required=True, max_length=255)
    note = StringField(max_length=255)

class Host(Document):
    hostname = StringField(required=True, max_length=255)
    pub_ip = IPAddrField(required=True)
    pri_ip = IPAddrField()
    idc = ReferenceField(reference_document_type=Idc)
    active = BooleanField(required=True, default=True)
    cost = FloatField(required=True, default=0.0)
    online = DateTimeField(required=True, auto_now_on_insert=True)
    update = DateTimeField(required=True, auto_now_on_insert=True, 
                           auto_now_on_update=True)
    offline = DateTimeField()
    hw_info = JsonField()
    note = StringField(max_length=255)