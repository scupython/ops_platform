#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *

def _ret_json(json):
    return json
    
def get_game_of_user(user):

    gs = Game.objects.find_all(callback=_ret_json)

    