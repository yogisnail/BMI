# BMI
 This code is calculating a person's BMI (Body Mass Index), BMR (Basal Metabolic Rate) and daily calorie needs based on inputs like height, weight, age, gender and activity level.

*Here is a simple explanation of what it is doing:

1.Defines 4 functions:
calculate_bmi: Calculates BMI based on weight and height
calculate_bmr: Calculates BMR based on weight, height, age and gender
calculate_calories: Calculates daily calorie needs based on BMR and activity level
main: The main function that runs the program
2.The main function:
Asks user to input height, weight, age, gender and activity level
Calls calculate_bmi and prints the BMI
Calls calculate_bmr and prints the BMR
Calls calculate_calories to calculate calorie needs
Prints recommended daily calories for the user
3.The calculate_bmi function calculates the BMI using the standard formula: weight (kg) / (height (m))^2
4.The calculate_bmr function calculates BMR based on well-known formulas that differ for men and women.
5.The calculate_calories function calculates calories by multiplying the BMR by an activity factor that varies based on the person's activity level.
 So in summary, it takes user inputs, applies medical formulas for BMI and BMR, calculates calories needed and prints out a weight/nutrition recommendation for the person.
