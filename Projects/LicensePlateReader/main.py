import os
import subprocess

def main():
    image_path = './data/located_plates/cropped_image.png'

    try:
        print("running script....")
        subprocess.run(['python', './locate_plate.py'], check=True)

        if not os.path.exists(image_path):
            print('no license palte image detected')
            return
    
        print(f"License plate detected... saved at {image_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error while running...{e}")

    
    try:
        print("locating text...")
        subprocess.run(['python', './get_text.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script...{e}")

if __name__ == "__main__":
    main()