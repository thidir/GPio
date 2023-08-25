import time

def traffic_light():
    while True:
        print("Red light")
        time.sleep(5)  # Red light for 5 seconds
        
        print("Green light")
        time.sleep(5)  # Green light for 5 seconds
        
        print("Yellow light")
        time.sleep(2)  # Yellow light for 2 seconds

if __name__ == "__main__":
    traffic_light()
