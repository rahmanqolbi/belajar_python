from tkinter import Widget
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    nama = ObjectProperty(None)        
    kelas = ObjectProperty(None)        

    def tekan(self):
        nama = self.nama.text
        kelas = self.kelas.text
        #self.add_widget(Label(
        print(f"Nama saya {nama} kelas {kelas}")
        self.nama.text = ""
        self.kelas.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

MyApp().run()