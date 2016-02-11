import sys

try:
    from django.conf import settings
    from django.test.utils import get_runner

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="cmsplugin_plain_text.urls",
        LANGUAGE_CODE='en',
        LANGUAGES=(
            ('en', 'English'),
        ),
        CMS_LANGUAGES={
            1: [
                {
                    'code': 'en',
                    'name': 'English',
                    'public': True,
                },
            ],
            'default': {
                'hide_untranslated': False,
            },
        },
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            'django.contrib.admin',
            "cmsplugin_plain_text",
            "cms",
            "menus",
            "treebeard",
        ],
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(),
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.core.context_processors.debug',
                        'django.core.context_processors.i18n',
                        'django.core.context_processors.media',
                        'django.core.context_processors.static',
                        'django.core.context_processors.csrf',
                        'django.core.context_processors.tz',
                        'django.core.context_processors.request',
                        'django.contrib.messages.context_processors.messages',
                        'cms.context_processors.cms_settings',
                    ],
                    'loaders': [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]
                },
            },
        ]
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
