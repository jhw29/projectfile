print("20117894 조혜원\n")

def Kelvin_to_Fahrenheit(kelvin):
    return 1.8 * kelvin - 459.67

def Kelvin_to_Celsius(kelvin):
     return kelvin - 273.15

k = float(input())
print("화씨 : ", Kelvin_to_Fahrenheit(k))
print("섭씨 : ", Kelvin_to_Celsius(k))
