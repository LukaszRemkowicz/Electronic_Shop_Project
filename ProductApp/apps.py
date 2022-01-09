from django.apps import AppConfig


class ProductappConfig(AppConfig):
    name = 'ProductApp'

    def ready(self) -> None:
        import ProductApp.signals
