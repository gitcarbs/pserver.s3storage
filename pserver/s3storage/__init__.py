# -*- coding: utf-8 -*-
from plone.server import app_settings


def includeme(root):
    from . import storage
    app_settings['cloud_storage'] = "pserver.s3storage.interfaces.IS3FileField"