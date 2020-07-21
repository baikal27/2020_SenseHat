from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = round(sense.get_pressure(), 2)
print("pressure: {}".format(pressure))
sense.show_message(str(pressure))

humidity = round(sense.get_humidity(), 2)
print('humidity: {}'.format(humidity))
sense.show_message(str(humidity))

temp_humi = round(sense.get_temperature_from_humidity(), 2)
temp_press = round(sense.get_temperature_from_pressure(), 2)
print("temp_from_humidity: {}".format(temp_humi))
sense.show_message(str(temp_humi))
print("temp_from_pressure: {}".format(temp_press))
sense.show_message(str(temp_press))

sense.clear()
