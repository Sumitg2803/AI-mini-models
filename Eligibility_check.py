# Maharashtra Government Scheme Eligibility Checker

# Predefined data
income_limit = 800000   # annual income limit
allowed_regions = [
    # Major cities
    "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Thane",
    # All districts of Maharashtra
    "Ahmednagar", "Akola", "Amravati", "Beed", "Bhandara", "Buldhana", 
    "Chandrapur", "Dhule", "Gadchiroli", "Gondia", "Hingoli", "Jalgaon",
    "Jalna", "Kolhapur", "Latur", "Nanded", "Nandurbar", "Osmanabad",
    "Palghar", "Parbhani", "Raigad", "Ratnagiri", "Sangli", "Satara",
    "Sindhudurg", "Wardha", "Washim", "Yavatmal"
]
minimum_education = ["7th Pass", "10th Pass", "12th Pass", "Graduate", "Post Graduate", "PhD"]

# User input
age = int(input("Enter your age: "))
income = int(input("Enter your annual income (in Rs.): "))
region = input("Enter your district/city in Maharashtra: ").strip().title()
education = input("Enter your highest qualification (7th Pass/10th Pass/12th Pass/Graduate/Post Graduate/PhD): ").strip().title()

# Eligibility check with reasons
if age > 18 and income < income_limit and region in allowed_regions and education in minimum_education:
    print("✅ You are Eligible for the scheme.")
    print(f"Reason: Age is {age} (>18), income is {income} (<{income_limit}), region is {region} (valid), and education is {education} (meets requirement).")

else:
    reasons = []
    if age <= 18:
        reasons.append(f"Age is {age} (must be above 18).")
    if income >= income_limit:
        reasons.append(f"Income is {income} (must be below {income_limit}).")
    if region not in allowed_regions:
        reasons.append(f"Region '{region}' is not in the allowed Maharashtra districts.")
    if education not in minimum_education:
        reasons.append(f"Education '{education}' does not meet the minimum requirement (7th Pass or above).")
    
    if len(reasons) == 1:
        print("⚠️ You are Conditionally Eligible.")
    else:
        print("❌ You are Not Eligible.")
    
    print("Reason(s):")
    for r in reasons:
        print("-", r)
