def cal_bmi(weight,height):
    return weight/ ((height/100)**2)

def bmi_cat(bmi):
    if bmi<18.5:
        return "underweight"
    elif bmi <25:
        return "normal"
    elif bmi<30:
        return "overweight"
    else:
        return "obese"
    
def main():
    print("Welcome to BMI Calculator")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    bmi = cal_bmi(weight,height)
    category = bmi_cat(bmi)
    print(f'Your BMI is {bmi},which is {category}')
main()

    