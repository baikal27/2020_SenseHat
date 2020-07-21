import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import threading
from sense_hat import SenseHat

sensehatUi = 'SenseHat_base.ui'

class MainDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self, None)
		uic.loadUi(sensehatUi, self)

		self.t1 = threading.Thread(target=self.sensor_active)
		self.t1.start()
		self.sense_action = True
		print('sensor modules are activated.')

	def sensor_active(self):
		sense = SenseHat()
		sense.clear()

		pressure = round(sense.get_pressure(), 2)
		humidity = round(sense.get_humidity(), 2)
		temp_humi = round(sense.get_temperature_from_humidity(), 2)
		temp_press = round(sense.get_temperature_from_pressure(), 2)
		orien = sense.get_orientation()
		pitch = round(orien['pitch'], 3)
		roll = round(orien['roll'], 3)
		yaw = round(orien['yaw'], 3)

		self.temp_lcd.display(temp_press)
		self.humi_lcd.display(humidity)
		self.pitch_lcd.display(pitch)
		self.roll_lcd.display(roll)
		self.yaw_lcd.display(yaw)

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.t1.join()
			self.sense_action = False
			event.accept()
		else:
			event.ignore()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	dialog = MainDialog()
	dialog.show()
	sys.exit(app.exec_())

