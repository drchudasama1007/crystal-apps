# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from datetime import timedelta
from datetime import datetime


class CrystalReservation(http.Controller):


    @http.route('/reservation', type='http', auth="public", website=True)
    def crystal_reservation_page(self, **post):
        return http.request.render('crystal_reservation.reservation_template', {})

    @http.route('/thankyou', type='http', auth="public", website=True)
    def thankyou_page(self, **post):
        calendar = datetime.strptime(post.get('calendar'), "%Y-%m-%dT%H:%M") - timedelta(hours=5, minutes=30)
        if calendar:
            calendar = datetime.strftime(calendar, '%Y-%m-%d %H:%M')
        reservation = request.env['reservation.reservation'].sudo().create({
            'first_name': post.get('firstname'),
            'lastname': post.get('lastname'),
            'calendar': calendar,
            'email': post.get('email'),
            'phone': post.get('phone'),
            'no_guest': post.get('no_guest'),
            'no_children': post.get('no_children'),
            'dome': post.get('dome'),
        })
        return http.request.render('crystal_reservation.thankyou_template', {'reservation': reservation})
