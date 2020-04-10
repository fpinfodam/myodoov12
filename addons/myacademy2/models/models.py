# -*- coding: utf-8 -*-

from odoo import models, fields, api

class myacademy2(models.Model):
     _name = 'myacademy2.course'

     name = fields.Char(string="Title", required=True)
     description = fields.Text()

