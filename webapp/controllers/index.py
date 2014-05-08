#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.render('base.html')