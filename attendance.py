import os
import math

""""

total_classes = [42,30,62,45,32,56,34,45,34]

# total_classes = [24,18,27,20,38,27,22,32,22]

total_attendance = []

for class1 in total_classes:
    attended_classes = int(input(f"classes attended out of {class1}: "))
    attendance_percentage = (attended_classes / class1) * 100
    total_attendance.append(attendance_percentage)

print(sum(total_attendance)/len(total_attendance))

"""

# Program to calculate safe skips per subject based on desired attendance percentage

import math

subjects = {
    "Chemistry": {"attended": 26, "total": 35, "slots_per_class": 1},
    "Chemistry Lab": {"attended": 18, "total": 26, "slots_per_class": 2},
    "Physics": {"attended": 30, "total": 38, "slots_per_class": 1},
    "Physics Lab": {"attended": 24, "total": 28, "slots_per_class": 2},
    "Python": {"attended": 40, "total": 54, "slots_per_class": 2},
    "Maths": {"attended": 30, "total": 39, "slots_per_class": 1},
    "Maths Lab": {"attended": 22, "total": 34, "slots_per_class": 2},
    "English": {"attended": 36, "total": 45, "slots_per_class": 1},
    "English Lab": {"attended": 26, "total": 30, "slots_per_class": 2},
}

desired_percentage = int(input("Enter desired attendance percentage (e.g., 90): "))

print(f"\nMaximum classes you can skip per subject to maintain ≥{desired_percentage}% attendance:\n")

for subject, data in subjects.items():
    total = data["total"]
    slots_per_class = data["slots_per_class"]

    # Minimum classes required
    min_attend = math.ceil(total * desired_percentage / 100)
    
    # Maximum classes you can skip in the semester
    remaining_skip_classes = total - min_attend
    
    # Equivalent slots for labs
    remaining_skip_slots = remaining_skip_classes * slots_per_class
    
    print(f"{subject}: {remaining_skip_classes} classes can be skipped ({remaining_skip_slots} slots)")


