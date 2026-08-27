{
    'name': 'Tulip Livechat Button Hover Color',
    'version': '17.0.1.0.0',
    'category': 'Website/Live Chat',
    'summary': 'Change hover color of buttons inside Live Chat to #00B3C6',
    'description': 'Overrides hover color for all buttons inside the Odoo Live Chat embed.',
    'author': 'Tulip-tech',
    'website': 'https://tulip-tech.com',
    'license': 'LGPL-3',
    'price': 1.0,
    'currency': 'USD',
    'depends': ['im_livechat'],
    'data': [],
    'assets': {
        'im_livechat.assets_embed_core': [
            'tulip_livechat_button_color/static/src/scss/livechat_button_hover.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
