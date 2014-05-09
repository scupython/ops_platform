#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
from urllib.request import urlopen
import json
from .base import BaseHandler
from tornado.web import RequestHandler

import logging
logger = logging.getLogger('elexops.' + __name__)

class CasClientMixin(object):
    @property
    def cas_server_url(self):
        return 'http://passport.xingcloud.com'

    @property
    def service_url(self):
        return "%s://%s/login?next=%s" % (self.request.protocol, 
                                          self.request.host, 
                                          self.get_next_url())

    def get_next_url(self, default='/'):
        return self.get_argument('next', default)

    def get_login_url(self):
        params = {'service': self.service_url}
        return '%s/login?%s' % (self.cas_server_url, urlencode(params))

    def get_logout_url(self):
        url = '%s/logout?service=%s://%s' % (self.cas_server_url,
                                             self.request.protocol,
                                             self.request.host)

        return url

    def verify_cas(self, *args, **kwargs):
        return self._verify_cas3(*args, **kwargs)

    # https://bitbucket.org/cpcc/django-cas/src/default/django_cas/backends.py
    def _verify_cas3(self, ticket, service):
        """Verifies CAS 3.0+ XML-based authentication ticket and returns extended attributes.

        Returns username on success and None on failure.
        """

        try:
            from xml.etree import ElementTree
        except ImportError:
            from elementtree import ElementTree

        params = {'ticket': ticket, 'service': service}
        url = '%s/proxyValidate?%s' % (self.cas_server_url, urlencode(params))
        page = urlopen(url)
        try:
            user = None
            response = page.read()
            #logger.debug(response)
            tree = ElementTree.fromstring(response)
            if tree[0].tag.endswith('authenticationSuccess'):
                for element in tree[0]:
                    if element.tag.endswith('user'):
                        user = element.text

            return user
        finally:
            page.close()


class LoginHandler(CasClientMixin, BaseHandler):
    def get(self):
        ticket = self.get_argument('ticket', None)
        if ticket:
            username = self.verify_cas(ticket, self.service_url)
            if username:
                self.set_secure_cookie('cas_user', username)
                #logger.debug(self.get_next_url())
                return self.redirect(self.get_next_url())
        return self.redirect(self.get_login_url())


class LogoutHandler(CasClientMixin, BaseHandler):
    def get(self):
        self.clear_cookie('cas_user')
        return self.redirect(self.get_logout_url())