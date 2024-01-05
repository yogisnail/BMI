def calculate_bmi(weight, height_cm):

    height_m = height_cm / 100  
    bmi = weight / (height_m ** 2)
    return bmi

def calculate_bmr(weight, height_cm, age, gender):

    height_m = height_cm / 100  
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_m * 100) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_m * 100) - (4.330 * age)
    else:
        raise ValueError("Gender should be 'male' or 'female'.")
    return bmr

def calculate_calories(bmr, activity_level):

    activity_multipliers = {'sedentary': 1.2, 'lightly_active': 1.375, 'moderately_active': 1.55, 'very_active': 1.725}
    calories = bmr * activity_multipliers[activity_level]
    return calories

def main():

    height_cm = float(input("Please enter your height in centimeters: "))  
    weight = float(input("Please enter your weight in kilograms: "))
    age = int(input("Please enter your age: "))

    print("Select your gender:")
    print("1. Male")
    print("2. Female")
    gender_choice = input("Enter the number corresponding to your gender: ")
    gender = 'male' if gender_choice == '1' else 'female'

    print("Select your daily activity level:")
    print("1. Sedentary")
    print("2. Lightly Active")
    print("3. Moderately Active")
    print("4. Very Active")
    activity_choice = input("Enter the number corresponding to your activity level: ")
    activity_levels = ['sedentary', 'lightly_active', 'moderately_active', 'very_active']
    activity_level = activity_levels[int(activity_choice) - 1]

    bmi = calculate_bmi(weight, height_cm)
    print(f"Your BMI: {bmi:.2f}")

    bmr = calculate_bmr(weight, height_cm, age, gender)
    print(f"Your BMR: {bmr:.2f} calories per day")

    calories = calculate_calories(bmr, activity_level)
    print(f"To maintain your weight, you need to consume {calories:.2f} calories per day.")

if __name__ == "__main__":
    main()
