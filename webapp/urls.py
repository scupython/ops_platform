#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers.index import IndexHandler
from controllers.cas_client import LoginHandler, LogoutHandler
url_patterns = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler)
]