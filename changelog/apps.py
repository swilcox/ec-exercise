from django.apps import AppConfig


class ChangelogConfig(AppConfig):
    name = 'changelog'

    def ready(self):
        from .signals import pre_save_handler
        pass
