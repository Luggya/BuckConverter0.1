
import math
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.theming import ThemeManager
from sympy import symbols,Eq,solve

from kivy.core.window import Window
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

class MyMainScreen(Screen):
	#THIRD SCREEN CLEAR FIELD
	def clear_field1(self):
		self.ids.field1.text=""
		self.ids.box1.active=False
		if self.ids.field1.text=="":
			self.ids.field1.focus=True
			
	def clear_field2(self):
		self.ids.field2.text=""
		self.ids.box2.active=False
		if self.ids.field2.text=="":
			self.ids.field1.focus=True
			
	def clear_field3(self):
		self.ids.field3.text=""
		self.ids.box3.active=False
		if self.ids.field3.text=="":
			self.ids.field1.focus=True
	
	def clear_field4(self):
	   self.ids.field4.text=""
	   self.ids.box4.active=False
	   if self.ids.field4.text=="":
    		self.ids.field1.focus=True
	
	def clear_field5(self):
	   self.ids.field5.text=""
	   self.ids.box5.active=False
	   if self.ids.field5.text=="":
    		self.ids.field1.focus=True
      		
	def clear_field6(self):
	    self.ids.field6.text=""
	    self.ids.box6.active=False
	    if self.ids.field6.text=="":
    		self.ids.field1.focus=True
    
	def clear_field7(self):
	    self.ids.field7.text=""
	    self.ids.box7.active=False
	    if self.ids.field7.text=="":
	    	self.ids.field1.focus=True
	
	def clear_field8(self):
	    self.ids.field8.text=""
	    self.ids.box8.active=False
	    if self.ids.field8.text=="":
	    	self.ids.field1.focus=True
	
	def clear_field9(self):
	    self.ids.field9.text=""
	    self.ids.box9.active=False
	    if self.ids.field9.text=="":
	    	self.ids.field1.focus=True
     
     
    #THIRD SCREEN CHECK BOX	   		    
	def check1(self):
	   if self.ids.field1.text:
	   	self.ids.box1.active=True   
    			
	def check2(self):
	   if self.ids.field2.text:
    		self.ids.box2.active=True
    		
	def check3(self):
	   if self.ids.field3.text:
    		self.ids.box3.active=True
    
	def check4(self):
	   if self.ids.field4.text:
	   	self.ids.box4.active=True
	
	def check5(self):
		if self.ids.field5.text:
			self.ids.box5.active=True
	
	def check6(self):
		if self.ids.field6.text:
			self.ids.box6.active=True
	
	def check7(self):
		if self.ids.field7.text:
			self.ids.box7.active=True
	
	def check8(self):
		if self.ids.field8.text:
			self.ids.box8.active=True
	
	def check9(self):
		if self.ids.field9.text:
			self.ids.box9.active=True
    		
    		
class MyScreenManager(ScreenManager):
	pass

class MySecondScreen(Screen):
	pass

class MyThirdScreen(Screen):
	pass

class Content(MDBoxLayout):
    """ """
	
class CustomToolbarMain(
    MDBoxLayout,ThemableBehavior, RectangularElevationBehavior
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = 76/255,145/255,65/255,1

class CustomToolbar2(
    MDBoxLayout,ThemableBehavior, RectangularElevationBehavior
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = 237/255,118/255,14/255,1

class CustomToolbar3(
    MDBoxLayout,ThemableBehavior, RectangularElevationBehavior
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = 108/255,81/255,221/255,1
        
        
class BuckConverter(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.screen=Builder.load_file("buckconverter1.kv")
	
	dialog =None
	def my_dialog(self):
		self.dialog= MDDialog(
    			title= "[b]Calculated Results[/b]",
    			type="custom",
    			auto_dismiss=False,
    			content_cls=Content(),
    			buttons=[
    				MDFlatButton(
    					text="SHARE",
    					font_size=16,
    					font_name="Helvetica LT 97 Black Condensed.ttf",
    					text_color=(76/255,145/255,65/255,1)		
    				),
    				MDFlatButton(
    					text="CANCEL",
    					font_name="Helvetica LT 97 Black Condensed.ttf",
    					font_size=16,
    					text_color=(76/255,145/255,65/255,1),
    					on_release=self.dialog_close
    				)
    			
    			]
    		)
    		
		self.dialog.open()
	
	def dialog_close(self,*args):
		self.dialog.dismiss(force=True)	  
	
	
	#MYCALCULATIONS
	def MyCalculations(self):
		if self.screen.get_screen("main_screen").ids.field1.text=="":
		    self.snackbar= Snackbar(text="Please  InPut Voltage Field is Missing!")
		    self.snackbar.show()
		
		elif self.screen.get_screen("main_screen").ids.field2.text=="":
		    self.snackbar= Snackbar(text="Please  OutPut Voltage Field is Missing!")
		    self.snackbar.show()
		    
		elif self.screen.get_screen("main_screen").ids.field3.text=="":
		    self.snackbar= Snackbar(text="Please  OutPut Current  Field is Missing!")
		    self.snackbar.show()
		
		elif self.screen.get_screen("main_screen").ids.field4.text=="":
		    self.snackbar= Snackbar(text="Please  Ripple Current Field is Missing!")
		    self.snackbar.show()
	   
		elif self.screen.get_screen("main_screen").ids.field5.text=="":
		    self.snackbar= Snackbar(text="Please  Ripple Voltage Field is Missing!")
		    self.snackbar.show()
		
		elif self.screen.get_screen("main_screen").ids.field6.text=="":
		    self.snackbar= Snackbar(text="Please  Efficiency Field is Missing!")
		    self.snackbar.show()
		
		elif self.screen.get_screen("main_screen").ids.field7.text=="":
		    self.snackbar= Snackbar(text="Please  Frequency Field is Missing!")
		    self.snackbar.show()
		    
		else:
			#POWER CALCULATIONS
			self.VOut=float(self.screen.get_screen("main_screen").ids.field2.text)
			self.IOut=float(self.screen.get_screen("main_screen").ids.field3.text)
			
			self.POut=(self.VOut*self.IOut)
			POUT=f"   1].Output Power={self.POut:.2f} Watts"
			self.screen.get_screen("second_screen").ids.f1.text = str(POUT)
			
			#DUTY CYCLE CALCULATIONS
			self.Vin=float(self.screen.get_screen("main_screen").ids.field1.text)
			DutyCycle=(self.VOut/self.Vin)
			self.DutyCycle=round(DutyCycle*100)
			DUTYCYCLE=f"   2].DutyCycle = {self.DutyCycle} %"
			self.screen.get_screen("second_screen").ids.	f2.text = str(DUTYCYCLE)
			
			#RIPPLE CURRENT CALCULATIONS
			self.IRip=float(self.screen.get_screen("main_screen").ids.field4.text)
			self.IRipple=((self.IRip/100)*self.IOut)
			IRIPPLE=f"   3].Ripple Current = {self.IRipple:.2f} Amps"
			self.screen.get_screen("second_screen").ids.	f3.text = str(IRIPPLE)
			
			#INDUCTOR SIZE CALCULATIONS
			self.Fosc=float(self.screen.get_screen("main_screen").ids.field7.text)
			self.l=((self.VOut*(1-(DutyCycle)))/(self.Fosc*self.IRipple))*pow(10,6)
			L=f"   4].Inductor L = {self.l:.2f} uH"
			self.screen.get_screen("second_screen").ids.	f4.text = str(L)
			
			#RIPPLE VOLTAGE
			self.VRipple=float(self.screen.get_screen("main_screen").ids.field5.text)
			VRIPPLE=f"   5].Ripple Voltage = {self.VRipple} Volts"
			self.screen.get_screen("second_screen").ids.f5.text = str(VRIPPLE)
			
			#CAPACITOR SIZING
			self.VRipple=float(self.screen.get_screen("main_screen").ids.field5.text)
			self.Cap=round((self.IRipple)/(8*self.Fosc*self.VRipple)*pow(10,6))
			CAP=f"   6].Capacitor = {self.Cap} uF"
			self.screen.get_screen("second_screen").ids.f6.text = str(CAP)
			
			#SCHOTTKY AVERAGE CURRENT
			IDiode=self.IOut*(1-(self.DutyCycle/100))
			IDIODE=f"   7].Diode Current = {IDiode:.3f} Amps"
			self.screen.get_screen("second_screen").ids.	f7.text = str(IDIODE)
			
			#MOSFET AVERAGE CURRENT
			IMosfet=(self.IOut*(self.DutyCycle/100))
			IMOSFET=f"   8].Mosfet = {IMosfet:.3f} Amps"
			self.screen.get_screen("second_screen").ids.	f8.text = str(IMOSFET)
			
			#R1 FEEDBACK RESISTOR
			ICRef=float(self.screen.get_screen("main_screen").ids.field8.text)
			R2=float(self.screen.get_screen("main_screen").ids.field9.text)
			x=symbols("x")
			Equation=Eq(ICRef*(1+(x/R2)),self.VOut)
			self.FbR=solve(Equation)#Output is in a list
			FBR=f"   9].R1 Feedback = {self.FbR[0]:.1f} Ohms"
			self.screen.get_screen("second_screen").ids.f9.text = str(FBR)
			
			#SECOND SCREEN TEXT
			#LABEL1
			Label1=float(self.screen.get_screen("main_screen").ids.field1.text)
			LABEL1=f"   1].Input Voltage = {Label1} Volts"
			self.screen.get_screen("second_screen").ids.l1.text = str(LABEL1)
			
			#LABEL2
			Label2=float(self.screen.get_screen("main_screen").ids.field2.text)
			LABEL2=f"   2].Output Voltage = {Label2} Volts"
			self.screen.get_screen("second_screen").ids.l2.text = str(LABEL2)
			
			#LABEL3
			Label3=float(self.screen.get_screen("main_screen").ids.field3.text)
			LABEL3=f"   3].Output Current = {Label3} Amps"
			self.screen.get_screen("second_screen").ids.l3.text = str(LABEL3)
			
			#LABEL4
			Label4=float(self.screen.get_screen("main_screen").ids.field4.text)
			LABEL4=f"   4].Ripple Current = {Label4} % of IOut"
			self.screen.get_screen("second_screen").ids.l4.text = str(LABEL4)
			
			#LABEL5
			Label5=float(self.screen.get_screen("main_screen").ids.field5.text)
			LABEL5=f"   5].Ripple Voltage = {Label5} Volts"
			self.screen.get_screen("second_screen").ids.l5.text = str(LABEL5)
			
			#LABEL6
			Label6=float(self.screen.get_screen("main_screen").ids.field6.text)
			LABEL6=f"   6].Effieciency = {Label6} %"
			self.screen.get_screen("second_screen").ids.l6.text = str(LABEL6)
			
			#LABEL7
			Label7=float(self.screen.get_screen("main_screen").ids.field7.text)
			LABEL7=f"   7].Frequency = {Label7} Hz"
			self.screen.get_screen("second_screen").ids.l7.text = str(LABEL7)
			
			#LABEL8
			Label8=float(self.screen.get_screen("main_screen").ids.field8.text)
			LABEL8=f"   8].Ic Ref Voltage = {Label8} Volts"
			self.screen.get_screen("second_screen").ids.l8.text = str(LABEL8)
			
			#LABEL9
			Label9=float(self.screen.get_screen("main_screen").ids.field9.text)
			LABEL9=f"   9].Feedback R2 = {Label9} \u03A9"
			self.screen.get_screen("second_screen").ids.l9.text = str(LABEL9)
			
			
	#LOSSES AND EFFICIENCY CALCULATIONS
	def Losses(self):
		#1POWER IN
		Efficiency=float(self.screen.get_screen("main_screen").ids.field6.text)/100
		Pin=(self.POut/Efficiency)
		PIN=f"1].Input Power = {Pin:.2f} Watts"
		self.dialog.content_cls.ids.label1.text=str(PIN)
		
		#2OUTPUT POWER
		POUT=f"2].Output Power = {self.POut:.2f} Watts"
		self.dialog.content_cls.ids.label2.text=str(POUT)
		
		#3TOTAL POWER LOSS
		PTotal=(self.POut*((1/Efficiency)-1))
		PTOTAL=f"3].Ptotal Must be < {PTotal:.2f} Watts"
		self.dialog.content_cls.ids.label3.text=str(PTOTAL)
		
		#POUT/PIN MUST BE >EFFICIENCY
		PoutPin= Efficiency
		POUTPIN=f"4].Pout/Pin Must be > {PoutPin:.1f}"
		self.dialog.content_cls.ids.label4.text=str(POUTPIN)
		
		#INDUCTOR LOSSES''
		LESR=float(self.screen.get_screen("third_screen").ids.fld1.text)
		Pl=(pow(self.IOut,2)*LESR)
		PL=f"5].Inductor Losses = {Pl:.2f} mW"
		self.dialog.content_cls.ids.label5.text=str(PL)
		
		#DIODE LOSSES
		FDiode=float(self.screen.get_screen("third_screen").ids.fld2.text)
		Pd=(self.IOut*FDiode*(1-(self.DutyCycle/100)))*1000
		PD=f"6].Diode Losses = {Pd:.2f} mW"
		self.dialog.content_cls.ids.label6.text=str(PD)
	
		#MOSFET LOSSES
		Rds=float(self.screen.get_screen("third_screen").ids.fld3.text)
		
		#CONDUCTION LOSS
		Pc=(pow(self.IOut,2)*Rds*(self.DutyCycle/100))
		#PC=f"{Pc:.2f} mW"		
		#self.dialog.content_cls.ids.label6.text=str(PC)
	
		#SWITCHING LOSS
		ToN=float(self.screen.get_screen("third_screen").ids.fld4.text)
		ToFF=float(self.screen.get_screen("third_screen").ids.fld5.text)
		
		Ps=(((1/2)*self.Vin)*(self.IOut)*((ToN+ToFF)/pow(10,9))*self.Fosc)*1000
		#PS=f"{Ps:.2f} mW"
		#self.dialog.content_cls.ids.label6.text=str(PS)
	
		PMosfet=(Ps+Pc)
		PMOSFET=f"7].Mosfet Losses = {PMosfet:.2f} mW"
		self.dialog.content_cls.ids.label7.text=str(PMOSFET)
		
		#TOTAL POWER LOSS
		PTotal=(Pl+Pd+Ps)
		PTOTAL=f"8].Total Power Loss = {PTotal:.1f} mW"
		self.dialog.content_cls.ids.label8.text=str(PTOTAL)
		
		#CONVRTER EFFICIENCY
		Effic=round((self.POut/(self.POut+(PTotal/1000)))*100)
		EFFIC=f"9].Efficiency = {Effic}%"
		self.dialog.content_cls.ids.label9.text=str(EFFIC)
							 			 	
	
	def build(self):
	   	return self.screen
	
	
  
    

BuckConverter().run()