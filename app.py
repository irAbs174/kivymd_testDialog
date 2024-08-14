from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.metrics import sp
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogButtonContainer

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "سلام خوش آمدید"[::-1]
        halign: "center"
        font_style: "nasalization"
        pos_hint: {"center_x": .5, "center_y": .62}
    

    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "98dp", "42dp"
        on_release : app.showDialog()

        MDButtonIcon:
            icon: "plus"
            theme_icon_color: "Custom"
            icon_color: "green"

        MDButtonText:
            text : "شروع"[::-1]
            theme_font_name: "Custom"
            font_name: "assets/fonts/Lalezar-Regular.ttf"
            theme_font_size: "Custom"
            font_size: "20dp"


'''


class Example(MDApp):
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

        return Builder.load_string(KV)

    def showDialog(self):
        MDDialog(
            MDDialogHeadlineText(
                text="برای شروع وارد شده یا ثبت نام کنید"[::-1],
                halign="center",
                theme_font_name= "Custom",
                theme_font_size= "Custom",
                font_name= "assets/fonts/Lalezar-Regular.ttf",
                font_size= "40dp",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(
                        text= "ثبت نام"[::-1],
                        theme_font_name= "Custom",
                        theme_font_size= "Custom",
                        font_name= "assets/fonts/Lalezar-Regular.ttf",
                        font_size= "30dp",
                    ),
                    style="text",
                ),
                MDButton(
                    MDButtonText(
                        text= "ورود"[::-1],
                        theme_font_name= "Custom",
                        theme_font_size= "Custom",
                        font_name= "assets/fonts/Lalezar-Regular.ttf",
                        font_size= "30dp",
                    ),
                    style="text",
                ),
                spacing="8dp",
            ),
        ).open()

Example().run()