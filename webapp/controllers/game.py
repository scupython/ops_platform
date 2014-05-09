#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseHandler
from tornado import gen
from models.modelfunc import get_game_of_user
import logging
logger = logging.getLogger('elexops.' + __name__)

class GameIndexHandler(BaseHandler):

    def get(self):
        u = self.current_user
        games = get_game_of_user(u)
        self.render("game.html", games=games)

        
class GameInsertHandler(BaseHandler):
    pass