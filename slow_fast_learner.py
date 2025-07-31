# Function to calculate total percentage
def calculate_percentage(marks, total_marks=400):
    total = sum(marks)
    percentage = (total / total_marks) * 100
    return percentage

# Function to classify student
def classify_student(percentage):
    if percentage < 60:
        return "Slow Learner"
    elif 60 <= percentage <= 80:
        return "Average"
    else:
        return "Topper"

# Main function
def main():
    print("=== Student Performance Classification ===")
    
    # Taking input for marks in four subjects
    phy = float(input("Enter marks in Physics: "))
    maths = float(input("Enter marks in Maths: "))
    chem = float(input("Enter marks in Chemistry: "))
    bio = float(input("Enter marks in Biology: "))
    
    # List of marks
    marks = [phy, maths, chem, bio]
    
    # Calculate percentage
    percentage = calculate_percentage(marks)
    
    # Classify student based on percentage
    classification = classify_student(percentage)
    
    # Print the result
    print(f"\nTotal Percentage: {percentage:.2f}%")
    print(f"Student Classification: {classification}")

if __name__ == "__main__":
    main()