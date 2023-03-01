# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleScaffold(http.Controller):
#     @http.route('/module_scaffold/module_scaffold', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_scaffold/module_scaffold/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_scaffold.listing', {
#             'root': '/module_scaffold/module_scaffold',
#             'objects': http.request.env['module_scaffold.module_scaffold'].search([]),
#         })

#     @http.route('/module_scaffold/module_scaffold/objects/<model("module_scaffold.module_scaffold"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_scaffold.object', {
#             'object': obj
#         })
