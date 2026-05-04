from django.apps import AppConfig
from django.forms import widgets


class DjBosUIConfig(AppConfig):

    name = 'djbosui'

    def ready(self):

        # Monkey patch date/time inputs
        #
        widgets.DateTimeInput.input_type = 'datetime-local'
        widgets.DateInput.input_type = 'date'
        widgets.TimeInput.input_type = 'time'
