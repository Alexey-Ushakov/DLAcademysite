from django.apps import AppConfig


class AdvitoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advito'
    verbose_name = 'Адвито'

    def ready(self):
        from . import signals