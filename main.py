from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

Builder.load_file('screens.kv')
Builder.load_file('landing.kv')
Builder.load_file('home.kv')

class Screens(ScreenManager): 
	def __init__(self, **kwargs):
		super(Screens, self).__init__(**kwargs)
		self.current = 'landing'

	def navigate(self):
		self.current = 'home'

class Landing(Screen): 
	def __init__(self, **kwargs):
		super(Landing, self).__init__(**kwargs)
		self.name = 'landing'

class Home(Screen): 
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)
		self.name = 'home'

class MyPopup(Popup):
	def __init__(self, **kwargs):
		super(MyPopup, self).__init__(**kwargs)
	
	def navigateToHome(self):
		print(self)
		self.dismiss()
		

class MyApp(App):
	def build(self):
		self.title = 'MyApp'
		return Screens()

MyApp().run()