# Python Alarm Clock

import time
import datetime
import sounddevice as sd
import soundfile as sf

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = "After Dark.mp3"

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"\rCurrent Time: {current_time}", end="")

        if current_time == alarm_time:
            print("\nWake up!")

            try:
                data, samplerate = sf.read(sound_file)
                sd.play(data, samplerate)
                sd.wait()
            except Exception as e:
                print(f"Error playing sound: {e}")

            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)