from django.apps import AppConfig


class AdocaoConfig(AppConfig):
    name = 'adocao'

    def ready(self):
        # import signals to register signal handlers
        try:
            import adocao.signals  # noqa: F401
        except Exception:
            # avoid raising errors at import-time in environments running
            # migrations or when signals module is not available yet
            pass
