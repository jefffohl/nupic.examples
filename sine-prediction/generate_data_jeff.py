import csv
import math

ROWS = 1000

def run():
    fileHandler = open("sine.csv","w")
    writer = csv.writer(fileHandler)
    writer.writerow(["angle","sine"])
    writer.writerow(["float","float"])
    writer.writerow(["",""])

    for i in range(ROWS):
        angle = (i * math.pi) / 50.0
        sine_value = math.sin(angle)
        writer.writerow([angle, sine_value])

    fileHandler.close()

if __name__ == "__main__":
    run()
