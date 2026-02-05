#TempConvert.py
#Name: Jack Schulz
#Date: 2-5-2026
#Assignment: Lab 3 Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("What is the temperature in Fahreinheit?: ")
  tempF = float(tempF)

  tempC = (tempF - 32) * 5/9
  tempC = round(tempC,1)

  print(tempF, "degrees fahrenheit is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
