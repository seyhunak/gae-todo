from ragendja.settings_post import settings
settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'todo/code.js',
)

settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
)
