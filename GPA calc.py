# 🧮 Building a GPA calculator for WAEC students.

print("\t\t\t-----------------------------------------------------")
print("\t\t\t-----------------------------------------------------")
print()
print("\t\t\tWELCOME TO CHIJULY GPA CALCULATOR 😇")
print()
print("\t\t\t-----------------------------------------------------")
print("\t\t\t-----------------------------------------------------")
print()

# Login gate
log_in = input("Type YES to proceed: ")  # will login if the candidate inputs yes.

def log():
    print("Great. so what's next?")
if log_in.lower() == "yes":
    print("Login successful ✔️")
    
    # Candidate verification
    candidate_ID = input("Enter Candidate ID: ")  # only an ID that ends with AD can be granted access.
    if candidate_ID.endswith("AD"):
        log()
        print()

        # Step 3: Access the GPA portal
        print("\tNow let's get to your results 😁")
        print("\tSimply type 'Yes' to gain access.")  # 'Y' represents yes to gain final access.
        access_log_in = input("\tYes/No: ")
        print()

        if access_log_in.lower() == "yes":
            print("\t\t\tWEST AFRICAN EXAMINATION COUNCIL")
            print("\tName: CHINEDU PRINCE CHIMUANYA")
            print("\tCandidate ID:", candidate_ID)
            print("\tExamination Number: 2243523")
            log()
            print()

            # Ask if they want a sheet
            user_input = input("Do you want your result in sheet format? Type 'yes' to continue: ")

            if user_input.lower() == "yes":
                # Subjects and grades
                subjects = ["Radiology", "Neuroscience", "Endocrine physiology", "Rearch Ethics", "Pharmacology", "Gross Anatomy"]
                grades = ["A", "A", "B", "A", "A", "A"]

                # Grade points reference
                grade_points = {  
                    "A": 5,
                    "B": 4,
                    "C": 3,
                    "D": 2,
                    "E": 1,
                    "F": 0
                }    

                columns = 2
                cell_width = 15

                # Draw the top border
                print("+" + ("-" * cell_width + "+") * columns)

                # Draw each row with subject and grade
                for i in range(len(subjects)):
                    subject = subjects[i]
                    grade = grades[i]
                    print(f"| {subject:<13}| {grade:<13}|")
                    print("+" + ("-" * cell_width + "+") * columns)

                # ✅ Calculate GPA *after* the table
                total_points = 0
                for grade in grades:
                    total_points += grade_points.get(grade, 0)  # safe lookup
                GPA = total_points / len(grades)

                print()
                print("Your GPA is:", GPA)
                print("Congratulations Chinedu Prince! You passed your semester examination 🍾.")

            else:
                print("Okay! Sheet drawing cancelled 🚫")

        else:
            print("Access denied ❌. You chose not to continue.")

    else:
        print("Candidate ID incorrect 😕")

else:
    print("Thanks for checking CHIJULY GPA CALCULATOR! 😏")
