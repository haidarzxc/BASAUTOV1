import pandas as pd
class Systems():
	def __init__(self):
		self.tags=pd.DataFrame(columns=['Tag'])

	def addTag(self,tagName):
		self.tags.loc[len(self.tags.index)]=tagName

	def loadTags(self):
		# systems and equipment
		self.addTag("NETWORK")
		self.addTag("ENERGY")
		self.addTag("AHU")
		self.addTag("ZONE")
		self.addTag("CHILLER")
		self.addTag("BOILER")
		self.addTag("ELECPANEL")
		self.addTag("LIGHTING")
		
		# network
		self.addTag("DEVICE")
		self.addTag("CONNECTION")
		self.addTag("PROTOCOL")
		self.addTag("DEVICE_1REF")
		self.addTag("DEVICE_2REF")
		self.addTag("NETWORK_REF")

		# energy
		self.addTag("METER")
		self.addTag("ELEC")
		self.addTag("GAS")
		self.addTag("DOMESTIC")
		self.addTag("CILLED")
		self.addTag("MAKEUP")
		self.addTag("BLOWDOWN")
		self.addTag("CONDENSATE")
		self.addTag("STEAM")
		self.addTag("WATER")

		# AHUs
		self.addTag("HVAC")
		self.addTag("ROOFTOP")
		self.addTag("MAU")
		self.addTag("REF")

		# zone
		self.addTag("AIR")
		self.addTag("TEMP")
		self.addTag("SENSOR")
		self.addTag("HUMIDITY")
		self.addTag("CO2")
		self.addTag("EFFECTIVE")
		self.addTag("OCC")
		self.addTag("UNOCC")
		self.addTag("STANDBY")
		self.addTag("COOLING")
		self.addTag("HEATING")
		self.addTag("SP")

		# chillers
		self.addTag("CHILLED")
		self.addTag("LEAVING")
		self.addTag("ENTERING")
		self.addTag("DELTA")
		self.addTag("BYPASS")
		self.addTag("FLOW")
		self.addTag("PRESSURE")
		self.addTag("CONDENSER")
		self.addTag("VALVE")
		self.addTag("PRIMARY_LOOP")
		self.addTag("SECONDARY_LOOP")	
		self.addTag("EQUIPREF")	
		self.addTag("PLANT")	
		self.addTag("COOLED")	
		self.addTag("ABSORPTION")
		self.addTag("RECIPROCAL")
		self.addTag("SCREW")
		self.addTag("CENTRIFUGAL")
		self.addTag("COOLING_CAPACITY")
		self.addTag("ISOLATION")
		self.addTag("REF_RIG")
		self.addTag("CMD")
		self.addTag("COOLING_TOWER")
		self.addTag("OPEN_LOOP")
		self.addTag("CLOSED_LOOP")
		self.addTag("FAN")
		self.addTag("HEAT_EXCHANGER")
		
		# BOILERS
		self.addTag("HOT")
		self.addTag("MIXING")
		self.addTag("DAMPER")
		self.addTag("OUTSIDE")
		self.addTag("HEADER")
		self.addTag("FLUE")
		self.addTag("OIL")
		self.addTag("PUMP")
		
		# ELEC PANEL
		self.addTag("SITE_PANEL")
		self.addTag("SUB_PANEL_OF")
		self.addTag("ELEC_METER_REF")
		self.addTag("CIRCUIT")

		# LIGHTING
		self.addTag("LIGHTS")
		self.addTag("LIGHT_LEVEL")
		self.addTag("OCCUPANCY_INDICATOR")


		# others
		self.addTag("RETURN")

	def returnDuplicates(self, status):
		df=self.tags.duplicated(['Tag'])
		df=pd.concat([self.tags,df], axis=1, join="inner")
		df=df.rename(columns={"Tag": "Tag", 0: "Duplucates"})
		if(status==None):
			return df
		elif(status==True):
			return df.loc[df["Duplucates"]==True]
		elif(status==False):
			return df.loc[df["Duplucates"]==False]
	
	def analyzeRow(self,row):
		print(row)


	def retrievePoints(self,df):
		df.head(5).apply(self.analyzeRow, axis=1)

