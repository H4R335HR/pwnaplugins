from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import logging
import random

class HelloWorldPlugin(plugins.Plugin):
    __author__ = '@H4R335HR'
    __version__ = '0.0.1'
    __license__ = 'GPL3'
    __description__ = 'A simple plugin to display "Hello World" messages on Pwnagotchi'

    def on_loaded(self):
        logging.info("HelloWorldPlugin loaded")

    def on_ui_setup(self, ui):
        if ui.is_waveshare_v2():
            position = (0, 95)
        elif ui.is_waveshare_v3():
            position = (0, 95)
        elif ui.is_waveshare_v1():
            position = (0, 95)
        elif ui.is_waveshare144lcd():
            position = (0, 92)
        elif ui.is_inky():
            position = (0, 83)
        elif ui.is_waveshare27inch():
            position = (0, 153)
        else:
            position = (0, 91)

        orientation = self.options.get('orientation', 'horizontal')
        if orientation == "vertical":
            ui.add_element('hello-world', LabeledValue(color=BLACK, label='', value='',
                                                       position=position,
                                                       label_font=fonts.Bold, text_font=fonts.Small))
        else:
            ui.add_element('hello-world', LabeledValue(color=BLACK, label='', value='',
                                                       position=position,
                                                       label_font=fonts.Bold, text_font=fonts.Small))

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('hello-world')

    def on_ui_update(self, ui):
        messages = [
            "Hello World!",
            "Greetings from Pwnagotchi!",
            "Welcome to the hacking world!",
            "Pwnagotchi says hello!"
        ]

        if self.options.get('enabled', True):
            message = random.choice(messages)
        else:
            message = 'Hello World Plugin is disabled'

        ui.set('hello-world', message)
