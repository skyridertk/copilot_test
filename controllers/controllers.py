# -*- coding: utf-8 -*-
# from odoo import http


# class CopilotTest(http.Controller):
#     @http.route('/copilot_test/copilot_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copilot_test/copilot_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('copilot_test.listing', {
#             'root': '/copilot_test/copilot_test',
#             'objects': http.request.env['copilot_test.copilot_test'].search([]),
#         })

#     @http.route('/copilot_test/copilot_test/objects/<model("copilot_test.copilot_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copilot_test.object', {
#             'object': obj
#         })
