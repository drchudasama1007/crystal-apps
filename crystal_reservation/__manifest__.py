# -*- coding: utf-8 -*-
{
    'name': "Crystal Reservation",

    'summary': """
        Crystal Reservation
        """,

    'description': """
        Crystal Reservation
    """,

    'author': "Bansi Patel",

    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/mail.xml',
        'views/assets.xml',
        'views/reservation.xml',
        'views/reservation_views.xml',
        'views/footer.xml',
    ],
}
