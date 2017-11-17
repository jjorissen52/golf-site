from __future__ import absolute_import, unicode_literals
import os, configparser, socket

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for convenient
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", ("Media Library", "fb_browse"),)),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, "Top navigation bar", "pages/menus/dropdown.html"),
#     (2, "Left-hand tree", "pages/menus/tree.html"),
#     (3, "Footer", "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         ("Image",),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         ("Another name",),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the south application will be automatically added to the
# INSTALLED_APPS setting.

config = configparser.ConfigParser()
config.read(os.path.join(PROJECT_ROOT, 'secrets.conf'))
USE_SOUTH = True
SECRET_KEY = config.get('django', 'secret_key')

########################
# MAIN DJANGO SETTINGS #
########################

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'),
#                ('Full Name', 'anotheremail@example.com'))
ADMINS = (
    (config.get('golf_site', 'admin_name'), config.get('golf_site', 'admin_email')),
)
MANAGERS = ADMINS
ALLOWED_HOSTS = ["*"]
USE_TZ = True

LANGUAGE_CODE = "en"

# Supported languages
_ = lambda s: s
LANGUAGES = (
    ('en', _('English')),
)

DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1
USE_I18N = False
INTERNAL_IPS = ("127.0.0.1",)

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)
FILE_UPLOAD_PERMISSIONS = 0o644


CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATES = [
     {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
             # insert your TEMPLATE_DIRS here
             os.path.join(PROJECT_ROOT, "templates"),
             os.path.join(PROJECT_ROOT, "events/../events/templates"),
         ],
         'OPTIONS': {
             'context_processors': [
                 # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                 # list if you haven't customized them:
                 'django.contrib.auth.context_processors.auth',
                 'django.template.context_processors.debug',
                 # 'django.template.context_processors.i18n',
                 'django.template.context_processors.media',
                 'django.template.context_processors.request',
                 'django.template.context_processors.static',
                 'django.template.context_processors.tz',
                 'django.contrib.messages.context_processors.messages',
                 'mezzanine.pages.context_processors.page',
                 "mezzanine.conf.context_processors.settings",
                 "mezzanine.pages.context_processors.page",
             ],
             'loaders': [
                 # insert your TEMPLATE_LOADERS here
                 "django.template.loaders.filesystem.Loader",
                 "django.template.loaders.app_directories.Loader",
             ],
             'builtins': [
                 'mezzanine.template.loader_tags',
             ]
         },
     },
 ]


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    # "flat",
    # "moderna",
    # "nova",
    "solid",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.galleries",
    'events',
    'rest_framework',
    'storages',
    "compressor",
    # "mezzanine.twitter",
    #"mezzanine.accounts",
    #"mezzanine.mobile",
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)


try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

print(os.path.join(PROJECT_ROOT, "golf.db"))

if config.get('local', 'host_name') in HOSTNAME:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(PROJECT_ROOT, "golf.db"),
        }
    }
    STATIC_URL = '/static/'

else:
    ############# DATABASE DEFINITIONS ################
    SCHEMA = config.get('golf_site', 'db_schema')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'options': f'-c search_path={SCHEMA}'
            },
            'NAME': config.get('lambda', 'db_name'),
            'USER': config.get('lambda', 'db_user'),
            'PASSWORD': config.get('lambda', 'db_password'),
            'HOST': config.get('lambda', 'db_host'),
            'PORT': '5432',
        }
    }

############### FILE STORAGE CONFIG ###################
STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, '../static/'), os.path.join(PROJECT_ROOT, 'solid/../solid/static/')]
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root/')
COMPRESS_ROOT = STATIC_ROOT
AWS_LOCATION = 'content'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_HOST = "s3.us-east-1.amazonaws.com"
AWS_STORAGE_BUCKET_NAME = config.get('golf_site', 'storage_bucket_name')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#####################################################



####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())