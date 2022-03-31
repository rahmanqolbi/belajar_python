from cgitb import text
from winreg import KEY_ALL_ACCESS
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        # grid constractor
        super(MyGridLayout,self).__init__(**kwargs)
        
        # set columns
        self.cols = 2
        
        # add widgets
        self.add_widget(Label(text="Nama : "))
        # add input box
        self.nama = TextInput(multiline=False)
        self.add_widget(self.nama)

        # add widgets
        self.add_widget(Label(text="Kelas : "))
        # add input box
        self.kelas = TextInput(multiline=False)
        self.add_widget(self.kelas)

        # add Button
        self.simpan = Button(text="SIMPAN",font_size=32)
        # bind the button
        self.simpan.bind(on_press=self.tekan)
        self.add_widget(self.simpan)

    def tekan(self,instance):
        nama = self.nama.text
        kelas = self.kelas.text
        self.add_widget(Label(text=f"Nama saya {nama} kelas {kelas}"))
        self.nama.text = ""
        self.kelas.text = ""
class MyApp(App):
    def build(self):
        return MyGridLayout()

MyApp().run()