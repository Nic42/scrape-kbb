#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: util.py
"""
util.py
~~~~

Miscellaneous utility functions.
"""
__author__ = ["Andrew G. Dunn"]
__credits__ = ["Stephen Nettnin"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import requests

def construct_base_url(make, model, year, style):
    """ Take several arguments and construct a url
    """
    url = 'http://www.kbb.com/'

    url += make + '/'
    url += model + '/'
    url += year + '-' + make + '-' + model + '/'
    url += style + '/'

    return url


def url_fetch(url, intent, mileage):
    """ Not really ideal, maybe use **kwargs 
    """
    parameters = {}
    parameters['pricetype'] = intent
    parameters['mileage'] = mileage

    try:
        return requests.get(url, params=parameters)
    except Exception:
        return False

def parse_buy_new(url_payload):
    pass