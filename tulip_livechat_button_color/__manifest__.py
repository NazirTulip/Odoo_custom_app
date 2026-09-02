{
    'name': 'Tulip Livechat Button Hover Color',
    'version': '18.0.1.0.0',
    'category': 'Website/Live Chat',
    'summary': 'Recolour every button hover state inside the Odoo Live Chat widget',
    'description': """
Livechat Button Hover Color
===========================
Odoo lets you set the Live Chat channel colour, but the hover states inside the
chat window are not part of that setting. Buttons keep their default highlight,
which rarely matches the rest of the widget.

- Recolours the hover background, border and text of every button in the chat window.
- Covers the floating launcher bubble, with Odoo's default brightness filter removed.
- Registered on the Live Chat embed bundle only, so backend and website buttons are untouched.
- No models, no menus, no settings and no records created.

The colour is fixed in the stylesheet. Changing it means editing
static/src/scss/livechat_button_hover.scss and upgrading the module.
""",
    'author': 'TulipTech Ltd',
    'maintainer': 'TulipTech Ltd',
    'website': 'https://tulip-tech.com',
    'support': 'odoo@tulip-tech.com',
    'license': 'LGPL-3',
    'depends': ['im_livechat'],
    'data': [],
    'assets': {
        'im_livechat.assets_embed_core': [
            'tulip_livechat_button_color/static/src/scss/livechat_button_hover.scss',
        ],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
