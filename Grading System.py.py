def calculate_grade(score):
 if score >= 90:
  return 'A'
 elif 80 <= score < 90:
  return 'B'
 elif 70 <= score < 80:
  return 'C'
 elif 60 <= score < 70:
  return 'D'
 else:
  return 'F'
 def main():
  num_students = int(input("Enter the number of students: "))
 
 for i in range(1, num_students + 1):
  score = float(input(f"Enter the score of student {i}: "))
  grade = calculate_grade(score)
  print(f"Student {i}: Score = {score}, Grade = {grade}")
 if name == "main":
  main()
