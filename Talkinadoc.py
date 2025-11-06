# 💊 This is a questionnaire to assess and automate vital conditions of patients
# with just a simple yes/no response.


import time

print("\n\t\t\t--------MY TALKINADOC💊----------")

# 🔒 PASSWORD VERIFICATION
print("\n🔑 Patient password needed")
attempt = 0
while True:
    password = input("Input your password:  ")  # must end with MVC
    if password.endswith("MVC"):
        import time

        print("\n⏳ Verifying password...")
        time.sleep(1)
        print("\n📡 Beep...")
        time.sleep(1)
        print("📡 Beep...") 
        time.sleep(1)
        print("✅ Access granted! Welcome to MyTalkinaDoc 💊")  # the patient is granted access
        break
    else:
        attempt += 1
        final_attempt = 3
        current_attempt = final_attempt - attempt
        print("\n⏳ Verifying password...")
        time.sleep(1)
        print("\n📡 Beep...")
        time.sleep(1)
        print("📡 Beep...") 
        time.sleep(1)
        print("\n❌ Invalid password. You have", current_attempt, "more attempts.")
        if attempt == 3:
            print("🚫 Too many attempts. System locked 🔐", end=" ")  # system goes temporarily locked
            print("⏰ Try again in 10 minutes.")
            exit()

# ---------------------------------------------
# 🩺 MAIN PROGRAM STARTS
# ---------------------------------------------
print(
'''    
+--------------------------------------------+
|       👩‍⚕️ WELCOME TO "MY TALKINADOC" 🧑‍⚕️       |  
|          🧾 VITAL SIGNS QUESTIONNAIRE 🧬       |
+--------------------------------------------+
''')

all_batches = []  # List of batches (each batch = list of patients)

current_batch = []   # temporarily holds the first 5 patient's data 
                     # and sends to the all_batches after it reaches 5

batch_number = 1    # reflects the current patient we are in a 5 patient batch
patient_count = 0   # Keeps count of how many total patients entered across all batches

while True:
    print("\n🗂️ --- Batch " + str(batch_number) + " | Patient " + str(len(current_batch) + 1) + " ---")
    name = input("👤 Enter patient name: ")
    age = int(input("🎂 Enter patient age: "))
    sex = input("⚧ Enter patient sex (Male/Female): ")
    print("\n💬 Would you love to proceed to examination? Type yes.")
    decision = input("✅ Yes / ❌ No: ")

    if decision.lower() == "yes":

        # ============ 🥗 BMI / NUTRITION SECTION ============
        print("\n--- 🍎 Welcome to the BMI / Nutrition Assessment Section ---")
        bmi_questions = [
            "Do you often feel weak or tired? ",
            "Have you lost noticeable weight lately? ",
            "Do you get breathless climbing stairs? ",
            "Do you find your clothes tighter than before? ",
            "Do you eat balanced meals daily? "
        ]
        bmi_score = sum(input(q + "(yes/no): ").lower() == "yes" for q in bmi_questions)

        if bmi_score <= 1:
            bmi_status = "Underweight ⚠️"
            print("\n🩺 Your clinical report:", name, "From your evaluation, you seem to be diagnosed as Underweight.")
            print("\n💡 Essentials:")
            print("- 🍞 Take routine balanced meals rich in carbs and proteins.")
            print("- 🥛 Eat proteins like milk, egg, meat, and fish.")
            print("- 💧 Take minerals, vitamins, and water for immune defense.")
            print("- ⏱️ Practice 12-hour intermittent fasting weekly if possible.")
            print("- 🧑‍⚕️ Visit your physician regularly.")
        elif 2 <= bmi_score <= 3:
            bmi_status = "Normal ✅"
            print("\n", name, "👍 You seem to be doing well with your BMI.")
            print("\n💧 Keep up hydration habits (1–2L daily).")
        else:
            bmi_status = "Overweight ⚠️"
            print("\n🩺 Your clinical report:", name, "From your evaluation, you seem to be diagnosed as Overweight.")
            print("\n💡 Essentials:")
            print("\n- ❌ Reduce carbs and fats in meals.")
            print("\n- 🥗 Replace them with proteins, fruits, and water.")
            print("\n- 🧘 Stay active and practice 12-hour fasts weekly.")
            print("\n- 🧑‍⚕️ Visit your physician.")

        # ============ ❤️ PULSE SECTION ============
        print("\n--- 💓 Welcome to the Pulse / Heart Rate Assessment ---")
        pulse_questions = [
            "Do you feel your heart racing at rest? ",
            "Do you experience dizziness often? ",
            "Do you get palpitations or chest fluttering? ",
            "Do you exercise regularly? ",
            "Do you feel unusually fatigued? "
        ]
        pulse_score = sum(input(q + "(yes/no): ").lower() == "yes" for q in pulse_questions)

        if pulse_score <= 1:
            pulse_status = "Normal ❤️"
            print(name, "✅ You seem to be doing well with your pulse rate.")
        elif 2 <= pulse_score <= 3:
            pulse_status = "Mild irregularities ⚠️"
            print("\n🩺 Your clinical report:", name, "indicates mild pulse irregularities (~80–90bpm).")
            print("💡 Essentials:")
            print("\n- ☕ Reduce caffeine and nicotine.")
            print("\n- 🚭 Avoid unnecessary OTC drugs.")
            print("\n- 💧 Stay hydrated and eat fruits 🍉🍇🥒.")
        else:
            pulse_status = "Irregular pulse ❌"
            print("\n🚨 Your clinical report:", name, \
                  "indicates irregular pulse (~50–100bpm).")
            print("💡 Essentials:")
            print("\n- ❌ Stop caffeine and nicotine completely.")
            print("\n- 🧘 Practice relaxation and vagal breathing.")
            print("\n- 🍉 Eat electrolyte-rich fruits like watermelon and cucumber.")
            print("\n- 💧 Stay hydrated always.")

        # ============ 💉 BLOOD PRESSURE SECTION ============
        print("\n--- 🩸 Welcome to Blood Pressure Assessment ---")
        bp_questions = [
            "Do you have frequent headaches? ",
            "Do you experience blurred vision? ",
            "Do you feel dizzy when standing quickly? ",
            "Do your hands/feet swell often? ",
            "Do you consume salty foods regularly? "
        ]
        bp_score = sum(input(q + "(yes/no): ").lower() == "yes" for q in bp_questions)

        if bp_score <= 1:
            bp_status = "Normal ✅"
            print(name, "Your blood pressure appears normal.")
        elif 2 <= bp_score <= 3:
            bp_status = "Elevated ⚠️"
            print("\n⚠️ Elevated BP detected for", name, "(~180/120mmHg).")
            print("\n💡 Reduce salt, fat, and processed foods.")
            print("\n🏃‍♂️ Exercise regularly and drink more water.")
        else:
            bp_status = "High / Hypertensive ❌"
            print("\n🚨 Hypertension detected for", name, "(~200/130mmHg)!")
            print("\n⚕️ Visit your physician immediately.")
            print("\n🥦 Eat fruits, reduce fat and salt intake.")
            print("\n🚭 Quit smoking and alcohol.")

        # ============ 🍬 BLOOD SUGAR SECTION ============
        print("\n--- 🍩 Welcome to Blood Sugar Assessment ---")
        sugar_questions = [
            "Do you urinate frequently? ",
            "Do you feel excessive thirst? ",
            "Do you get shaky or dizzy before meals? ",
            "Have you lost weight without trying? ",
            "Do you feel sleepy after eating? "
        ]
        sugar_score = sum(input(q + "(yes/no): ").lower() == "yes" for q in sugar_questions)

        if sugar_score <= 1:
            sugar_status = "Normal ✅"
            print(name, "Your blood sugar appears normal.")
        elif 2 <= sugar_score <= 3:
            sugar_status = "Borderline / Monitor ⚠️"
            print("\n⚠️ Mild borderline increase in blood sugar (100–125 mg/dL).")
            print("\n🥦 Eat more veggies and complex carbs.")
            print("\n💧 Stay hydrated and limit sweets.")
        else:
            sugar_status = "High Sugar Level ❌"
            print("\n🚨 High blood sugar detected (126–200 mg/dL).")
            print("\n🍏 Eat fiber-rich foods and reduce carbs.")
            print("\n🚭 Quit smoking and alcohol.")
            print("\n💧 Drink water frequently.")

        # ============ 🗂️ STORE IN CURRENT BATCH ============
        patient_data = [name, age, bmi_status, pulse_status, bp_status, sugar_status]
        current_batch.append(patient_data)
        patient_count += 1

        # ============ 📋 DISPLAY CLINICAL SHEET ============
        print("\n🧠 Processing data...⏳")
        time.sleep(1)
        print("\n📋 Generating clinical sheet...")
        time.sleep(1)
        print("\n+---------------------------------------+")
        print("|         🩺 MY TALKINADOC CLINICAL SHEET |")
        print("+---------------------------------------+")
        print("| 👤 Name: ", name)
        print("| 🎂 Age: " + str(age))
        print("| 🥗 BMI / Nutrition: " + bmi_status)
        print("| ❤️ Pulse / Heart: " + pulse_status)
        print("| 💉 Blood Pressure: " + bp_status)
        print("| 🍬 Blood Sugar: " + sugar_status)
        print("+---------------------------------------+")

        # ✅ Auto-create new batch every 5 patients
        if len(current_batch) == 5:
            print("\n📦 Batch " + str(batch_number) + " completed ✅")
            all_batches.append(current_batch)
            current_batch = []
            batch_number += 1

        next_patient = input("\n➕ Add another patient? (yes/no): ").lower()
        if next_patient != "yes":
            if current_batch:
                all_batches.append(current_batch)
            break

# ============ 📊 DISPLAY ALL BATCHES ============
print("\n\n===== 📁 ALL BATCHES SUMMARY =====")
for i, batch in enumerate(all_batches, start=1):
    print("\n🗂️ Batch " + str(i) + " Summary (" + str(len(batch)) + " patients)")
    print("+----------------------------------------------------------------------------------------------+")
    print("| "
        + "Name".ljust(18)
        + "Age".ljust(8)
        + "BMI".ljust(20)
        + "Pulse".ljust(22)
        + "BP".ljust(18)
        + "Sugar".ljust(25)
        + "|"
    )
    print("+----------------------------------------------------------------------------------------------+")

    for patient in batch:
        name = str(patient[0]).ljust(18)
        age = str(patient[1]).ljust(8)
        bmi_status = str(patient[2]).ljust(20)
        pulse_status = str(patient[3]).ljust(22)
        bp_status = str(patient[4]).ljust(18)
        sugar_status = str(patient[5]).ljust(25)

        print("| " + name + age + bmi_status + pulse_status + bp_status + sugar_status + "|")

    print("+----------------------------------------------------------------------------------------------+")

print("\t\t\t--------🎉 THANK YOU FOR USING TALKINaDOC 💊 -----------")
print("\n\t\t\t\t\t\t\t\t🌿 \"Good health is true wealth.\" 🌿")
