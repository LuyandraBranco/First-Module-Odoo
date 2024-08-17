{
    'name': 'Meu Módulo',
    'version': '16.0.1.0.0',
    'summary': 'Um breve módulo pra treinar',
    'sequence': 10,
    "author": "Luyandra Branco",
    'description': """
        Nada por comentar.
    """,
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/modelo_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
