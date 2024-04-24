
name = input(" Hello what is your name ? ")
UserWeight = float(input(f" hey {name} how much your weight?" ))
UserHeight = float(input(" and what is your height ?"))

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_type(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

bmi_result = calculate_bmi(UserWeight,UserHeight)
type = bmi_type(bmi_result)

print(f"you bmi is {bmi_result} and you are {type} .")