# A simple program to test the driver

import time
import HTU21DF

while True:
	print("sending reset...")
	HTU21DF.htu_reset
	temperatureC = HTU21DF.read_temperatureC()
	print("The temperature is %f C." % temperatureC)
	time.sleep(1)
	temperatureF = HTU21DF.read_temperatureF()
	print("The temperature is %f F." % temperatureF)
	time.sleep(1)
	humidity = HTU21DF.read_humidity()
	print("The humidity is %F percent." % humidity)
	time.sleep(1)
