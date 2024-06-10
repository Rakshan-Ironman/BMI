height=float(input("please enter your height"))
weight=float(input("please enter your weight"))
BMI=weight/(height**2)
if (BMI<18.5):
    print("You are under weight")
elif (BMI>=18.5)and(BMI<24.9):
    print("you are normal weight")
elif (BMI>25)and(BMI<29.9):
    print("you are over weight")
elif (BMI>=30):
    print("you have obesity")
print(BMI)
