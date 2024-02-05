from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ClassyConnect(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols = 1
		self.window.size_hint=(0.7, 0.85) #margins
		self.window.pos_hint={"center_x":0.5, "center_y":0.5} #position
		
		from kivy.core.window import Window
		Window.size = (450, 600)
		
		#icon image
		self.img = Image(source='logo1.png', size_hint=(4,4))
		self.window.add_widget(self.img)
		
		#greetingText
		self.greetingText = Label(
								text="Hey! What's your Batch?", 
								font_size=18,
								color="00FFCE"
								)
		self.window.add_widget(self.greetingText)
		
		#input
		self.batchInput=TextInput(
								multiline=False,
								padding_y=(5,5), 
								padding_x=(150, 30),
								size_hint=(0.5,0.8),
								font_size=18,
								)
		self.window.add_widget(self.batchInput)
		
		
		#button
		self.nextClassButton = Button(
									text="Show next class",
									size_hint=(1,1),
									bold=True,
									background_color="#00FCE",
									font_size=18
									)
		self.nextClassButton.bind(on_press = self.logic)
		self.window.add_widget(self.nextClassButton)
		
		#clearbutton
		self.clearButton = Button(
								text="Clear",
								size_hint=(1,0.7),
								bold=True,
								background_color="#f50505",
								)
		self.clearButton.bind(on_press = self.clearFunc)
		self.window.add_widget(self.clearButton)
		
		#SubjectText
		self.subText = Label(
							text="", 
							font_size=17,
							color="00FFCE",
							size_hint=(0.5,0.5)
							)
		self.window.add_widget(self.subText)
		
		#TimeText
		self.timeText = Label(
							text="", 
							font_size=17,
							color="00FFCE",
							size_hint=(0.5,0.5)
							)
		self.window.add_widget(self.timeText)
		
		#locationText
		self.locText = Label(
							text="", 
							font_size=17,
							color="00FFCE",
							size_hint=(0.5,0.5)
							)
		self.window.add_widget(self.locText)
		
		
		return self.window
	
	def clearFunc(self, event) : 
		self.subText.text = ""
		self.locText.text = ""
		self.timeText.text = "" 
		self.batchInput.text = ""
		
	
	def logic(self, event) :
		#self.greetingText.text = "Hello " + self.nameInput.text + "!"
		#self.nameInput.text=""
		
		import pandas as pd
		from datetime import datetime

		#getting current time in hours and minutes
		now = datetime.now()
		curTime = now.strftime("%H:%M")

		#curTime="08:00"
		print("current time:",curTime)

		#Getting today's day in 3 letter format : eg-MON, SUN
		curDay = datetime.today().strftime("%a")
		curDay = curDay.upper()

		print(curDay)


		#batch
		b=self.batchInput.text
		b=b.upper()
		b="SY"+b
		print("your batch is", b)

		#class
		c=b[0:3]
		print("class:",c)

		#converting excel file to a dataframe
		df1 = pd.read_excel('TimeTable.xlsx')

		cnt = 0

		#main loop
		for i in range(1, len(df1)):
			if(df1.iloc[i,0] == curDay):

				for j in range(1,len(df1.columns)):
					if (df1.iloc[i,j] == c or df1.iloc[i,j]==b):
						cName = df1.iloc[i,j+1]
						cLoc = df1.iloc[i+1,j]
						cTime = str(df1.iloc[0,j])


						if (curTime<=cTime and cnt==0):
							print(cName)
							print(cLoc)
							cTime = datetime.strptime(cTime, '%H:%M:%S')
							cTime = datetime.strftime(cTime,"%I:%M")
							print(cTime)
							
							self.subText.text = "Subject  :  " + cName 
							self.locText.text = "Class  :  " + cLoc
							self.timeText.text = "Time  :  " + cTime
						
							cnt=cnt+1
							
							

obj = ClassyConnect()
obj.run()
