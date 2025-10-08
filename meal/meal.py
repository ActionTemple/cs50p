
# Meal times
# Andrew Waddington






def main():
  time = input("What time is it? ")
  t = convert(time)
  if 07.0 <= t <= 08.0:
    print ("breakfast time")
  elif 12.0 <= t <= 13.0:
    print ("lunch time")
  elif 18.0 <= t <= 19.0:
    print ("dinner time")


def convert(time):
  hours, minutes = time.split(":")
  h = int (hours)
  m = int (minutes)
  min = float (m/60)
  t= float (h + min)
  return (t)


if __name__ == "__main__":
  main()

