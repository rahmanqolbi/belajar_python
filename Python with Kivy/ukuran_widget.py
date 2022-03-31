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
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # buat grid layout kedua
        self.grid_atas = GridLayout(
            row_force_default = True,
            row_default_height = 40,
            col_force_default = True,
            col_default_width = 100
        )
        self.grid_atas.cols = 2
        
        # add widgets
        self.grid_atas.add_widget(Label(text="Nama : ",))
        # add input box
        self.nama = TextInput(multiline=False,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 100)
        self.grid_atas.add_widget(self.nama)

        # add widgets
        self.grid_atas.add_widget(Label(text="Kelas : "))
        # add input box
        self.kelas = TextInput(multiline=False,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 100)
        self.grid_atas.add_widget(self.kelas)

        # menambahkan grid_atas ke aplikasi
        self.add_widget(self.grid_atas)
        # add Button
        self.simpan = Button(text="SIMPAN",
            font_size=32,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
            )
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