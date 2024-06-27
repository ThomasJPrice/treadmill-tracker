import time

def calculateDistance(speed, time):
  hours = time / 60
  distance = speed * hours
  return distance

distance = 0
print('Welcome to the Treadmill Distance Tracker!')
print('''
To start, simply:
- Enter the speed you ran at
- Enter how long you ran that speed for
- Repeat for all legs of the run
- Enter 0 for speed to stop''')

while True:
  speed = float(input("\nEnter the speed (km/h): "))

  if speed == 0:
    break
  
  time = float(input("Enter the time (mins): "))
  distance += calculateDistance(speed, time)

print(f"\nThe total distance is: {'%.2f' % distance}km")