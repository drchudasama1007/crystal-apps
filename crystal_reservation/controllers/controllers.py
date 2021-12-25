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
        print("=============post===================",post)
        # calendar = datetime.strptime(post.get('calendar'), "%Y-%m-%dT%H:%M") - timedelta(hours=5, minutes=30)
        # if calendar:
        #     calendar = datetime.strftime(calendar, '%Y-%m-%d %H:%M')
        reservation = request.env['reservation.reservation'].sudo().create({
            'first_name': post.get('firstname'),
            'lastname': post.get('lastname'),
            # 'calendar': calendar,
            'email': post.get('email'),
            'phone': post.get('phone'),
            'no_guest_sel': post.get('no_guest_sel') if post.get('no_guest_sel') else False,
            'no_children_sel': post.get('no_children_sel') if post.get('no_children_sel') else False,
            'time_slot': post.get('time_slot') if post.get('time_slot') else False,
            'reservation_date': post.get('reservation_date') if post.get('reservation_date') else False,
            'dome': post.get('imgbackground') if post.get('imgbackground') else False,
            # 'dome': post.get('dome'),
        })
        mail_template_reservation = request.env.ref('crystal_reservation.mail_template_reservation',
                                         raise_if_not_found=False)
        mail_template_reservation.sudo().send_mail(
            reservation.id, force_send=True, email_values={"email_to": reservation.email}
        )
        return http.request.render('crystal_reservation.thankyou_template', {'reservation': reservation})
