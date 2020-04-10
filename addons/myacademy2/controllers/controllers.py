# -*- coding: utf-8 -*-
from odoo import http

# class Myacademy2(http.Controller):
#     @http.route('/myacademy2/myacademy2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myacademy2/myacademy2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myacademy2.listing', {
#             'root': '/myacademy2/myacademy2',
#             'objects': http.request.env['myacademy2.myacademy2'].search([]),
#         })

#     @http.route('/myacademy2/myacademy2/objects/<model("myacademy2.myacademy2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myacademy2.object', {
#             'object': obj
#         })