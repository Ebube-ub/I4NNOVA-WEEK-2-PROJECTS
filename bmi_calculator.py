num1 = float(input("Enter Weight in kg: "))
feet = float(input("Enter Height in feet: "))
inches = float(input("Enter Height in inches: "))
height_in_meters = ((feet * 12)+ inches)*0.0254
bmi = num1 / (height_in_meters ** 2)
 
print("Your BMI is: " + str(bmi))
if bmi < 18.5:
    print("You are underweight, your health risk is minimal")
elif 18.5 <= bmi < 24.9:
    print("You are normal weight, your health risk is minimal")         
elif 25 <= bmi < 29.9:
    print("You are overweight, your health risk is increased")  
elif 30 <= bmi < 34.9:
    print("You are obese, your health risk is high")            
elif 35 <= bmi < 39.9:
    print("You are severly obese, your health risk is very high")    
else:
    print("You are morbidly obese, your health risk is extremely high") 
