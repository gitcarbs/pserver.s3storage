# -*- encoding: utf-8 -*-
from pserver.s3storage.interfaces import IInitialS3Upload
from pserver.s3storage.interfaces import IFinishS3Upload
from zope.interface import implementer
from zope.interface.interfaces import ObjectEvent


@implementer(IInitialS3Upload)
class InitialS3Upload(ObjectEvent):
    """An object has been created"""


@implementer(IFinishS3Upload)
class FinishS3Upload(ObjectEvent):
    """An object has been created"""
