from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'Search'

    def ready(self):
        import Search.signals