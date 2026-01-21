import time

alarm = input("Enter alarm time (H:M:S): ")

while True:
    current_time = time.strftime("%H:%M:%S")
    print("=====TIME=====")
    print(f"{current_time} | alarm: {alarm}")

    if current_time == alarm:
        print("Ringing")
        break

    time.sleep(1)
        