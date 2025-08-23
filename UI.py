from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFloatingActionButton
from threading import Thread
import subprocess
import sys

KV = '''
FloatLayout:

    FitImage:
        source: "Kurama.jpeg"

    MDFloatingActionButton:
        id: mic_button
        icon: "microphone-off"
        pos_hint: {"center_x": 0.5, "center_y": 0.36}
        md_bg_color: 0.275, 0.306, 0.31, 1
        on_release: app.toggle_kurama()

    MDFillRoundFlatIconButton:
        id: activate_button
        text: "Activate Kurama"
        icon: "robot"
        pos_hint: {"center_x": 0.5, "center_y": 0.26}
        font_size: "20sp"
        md_bg_color: 0.459, 0.518, 0.522, 1
        text_color: 1, 1, 1, 1
        on_release: app.toggle_kurama()
'''

class MyApp(MDApp):
    def build(self):
        self.kurama_process = None  # to store the process
        return Builder.load_string(KV)

    def toggle_kurama(self):
        """Toggle Kurama.py process on/off"""
        if self.kurama_process is None:
            # Start Kurama.py
            def target():
                self.kurama_process = subprocess.Popen(
                    [sys.executable, r"D:\Python\Kivy\KivyMd\Practice\Kurama\Kurama.py"]
                )
                self.kurama_process.wait()  # wait until process finishes
                self.kurama_process = None

            t = Thread(target=target, daemon=True)
            t.start()
            self.root.ids.activate_button.text = "Deactivate Kurama"
            self.root.ids.mic_button.icon = "microphone"
        else:
            # Stop Kurama.py
            self.kurama_process.terminate()
            self.kurama_process = None
            self.root.ids.activate_button.text = "Activate Kurama"
            self.root.ids.mic_button.icon = "microphone-off"

MyApp().run()
