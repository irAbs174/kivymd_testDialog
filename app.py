from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.button import MDButton, MDButtonText
from bidi.algorithm import get_display
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from arabic_reshaper import reshape
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.metrics import sp
from kivymd.app import MDApp


class UniqueApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        LabelBase.register(
            name="nasalization",
            fn_regular="assets/fonts/nasalization.otf",
        )

        self.theme_cls.font_styles["nasalization"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "nasalization",
                "font-size": sp(57),
            },
        }

        return Builder.load_file('templates/base.kv')

    def persian(self, txt):
        reshaped_text = reshape(txt)
        bidi_text = get_display(reshaped_text)
        return bidi_text

UniqueApp().run()