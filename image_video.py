from picamera2 import Picamera2
from gpiozero import LED
import time
import cv2
from PIL import Image

def image_at_time(img_dir, run_name, time_point):
    led = LED(pin = 17)
    
    with Picamera2() as picam2:
        led.on()
        camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
        picam2.configure(camera_config)
        picam2.capture_file(f"{img_dir}/images/{run_name}_time_{time_point}_hrs.jpeg")
        led.off()
    
    led.close()

def image_folder_to_video(img_dir, vid_dir, run_name):
    images = [img for img in os.listdir(img_dir) if img.endswith((".jpeg"))]

    # Set frame from the first image
    frame = cv2.imread(os.path.join(img_dir, images[0]))
    height, width, layers = frame.shape

    # Video writer to create .avi file
    video = cv2.VideoWriter(f'{vid_dir}/{run_name}.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))

    # Appending images to video
    for image in images:
        video.write(cv2.imread(os.path.join(img_dir, image)))

    # Release the video file
    video.release()
    cv2.destroyAllWindows()
