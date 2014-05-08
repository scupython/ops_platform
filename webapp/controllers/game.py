#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler
from tornado import gen
from models import Game, App
import logging
logger = logging.getLogger('elexops.' + __name__)

class GameInsertHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        game = yield Game.objects.create(
            name="testgame",
            cname="zhName",
            gametype='elex',
            active=1,
        )
        app = yield App.objects.create(
            name='testapp',
            cname='testapp_zh',
            game=game,
            active=1
        )
        self.write(str(app._id))
        self.finish()