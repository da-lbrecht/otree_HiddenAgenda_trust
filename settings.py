from os import environ

SESSION_CONFIGS = [
    dict(
        name='HiddenAgenda_trust',
        display_name="Hidden Agenda Trust App",
        app_sequence=['HiddenAgenda_trust'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=10.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8734889494145'

# Environment variables
DATABASE_URL = 'postgres://postgres@localhost/postgres'
OTREE_PRODUCTION = 1  # uncomment this line to enable production mode
OTREE_AUTH_LEVEL = 'DEMO'

INSTALLED_APPS = 'bootstrap4'