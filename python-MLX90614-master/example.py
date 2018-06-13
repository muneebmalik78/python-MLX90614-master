import streams
from mlx90614 import MLX90614

streams.serial()

thermometer_address = 0x5a

thermometer = MLX90614(thermometer_address)


while True:
		print thermometer.get_amb_temp()
		print thermometer.get_obj_temp() 
