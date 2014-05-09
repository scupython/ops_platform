#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler
import tornado
class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('base.html')