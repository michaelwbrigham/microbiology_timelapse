from picamera2 import Picamera2
from gpiozero import LED
import time

def image_at_time(img_dir, run_name, time_point):
    led = LED(pin = 17)
    
    with Picamera2() as picam2:
        led.on()
        camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
        picam2.configure(camera_config)
        picam2.capture_file(f"{img_dir}/images/{run_name}_time_{time_point}_hrs.jpeg")
        led.off()
    
    led.close()