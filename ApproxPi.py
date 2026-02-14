#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  piDecimals = input("how many decimals of pi would you like to be calculated?(1-10): ")
  piDecimals = int(piDecimals)
  isNumberValid = 1
  while isNumberValid == 1:
    if 1 <= piDecimals <= 10 :
      print("Sounds good!")
      isNumberValid = 2
    else:
      print("Invalid number, Try again.")
      piDecimals = input("How many decimals of pi would you like to be calculated?(1-10): ")
      piDecimals = int(piDecimals)
    

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, piDecimals) != round(realPi,piDecimals):
    #print(approxPi)
    approxPi = approxPi + (sign * 4 /denom)
    sign = sign * -1
    denom = denom +2

  end = time.time()

  elapsedTime = end - start
  elapsedTime = round(elapsedTime, 5)
  print(approxPi)
  print("It took", elapsedTime, "seconds")

if __name__ == '__main__':
  main()
