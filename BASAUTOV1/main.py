from hstack import Systems
import pandas as pd

def loadFile(path,sheet):
	xl = pd.ExcelFile(path)
	df = xl.parse(sheet)
	return df


if __name__ == '__main__':
	sys=Systems()
	sys.loadTags()
	# print(sys.tags)
	# print(sys.returnDuplicates(True))
	# sheet1=loadFile(".\data\Queens Museum Points List.xlsx","Sheet1")
	sheet2=loadFile(".\data\Floor1P.xlsx","Floor 1 points")
	sys.retrievePoints(sheet2)


