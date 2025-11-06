#dictionary

patients_data = [
    ("Chinedu", 23, "Normal"),   #keyword 0
    ("Deborah", 48, "Tuberclosis"), # keyword 1
    ("Sandra", 17, "Diabetes and Pneumonia"), #keyword 2
    ("Blessing", 21, "Dyspnea")  #keyword 3
]


def patients_dictionary():
    
    identity = ((input("Input keyword(1-3): ")))

    if identity == "0":
        print(
        f'''
       ========================================
                    PATIENT'S FILE
       ========================================
       | NAME       : {patients_data[0][0]}      
       | AGE        : {patients_data[0][1]}    
       | CONDITION  : {patients_data[0][2]}    
       ========================================
       ========================================
       ''')


        
    elif identity == "0a":
        print("Name of patient:", patients_data[0][0])

    elif identity == "0b":
        print("Age of patient:", patients_data[0][1])

    elif identity == "0c":
        print("Clinical condition:", patients_data[0][2])
    
    elif identity == "1":
         print(
        f'''
       ========================================
                    PATIENT'S FILE
       ========================================
       | NAME       : {patients_data[1][0]}      
       | AGE        : {patients_data[1][1]}   
       | CONDITION  : {patients_data[1][2]}    
       ========================================
       ========================================
       ''')
    
    elif identity == "1a":
        print("Name of patient:", patients_data[1][0])
    
    elif identity == "1b":
        print("Age of patient:", patients_data[1][1])
    
    elif identity == "1c":
        print("Clinical condition:", patients_data[1][2])

    elif identity == "2":
         print(
        f'''
       ========================================
                    PATIENT'S FILE
       ========================================
       | NAME       : {patients_data[2][0]}      
       | AGE        : {patients_data[2][1]}    
       | CONDITION  : {patients_data[2][2]}   
       ========================================
       ========================================
       ''')

    elif identity == "2a":
        print("Name of patient:", patients_data[2][0])           
    
    elif identity == "2b":
        print("Age of patient:", patients_data[2][1])
    
    elif identity == "2c":
        print("Clinical condition:", patients_data[2][2])

    else:
        print("Keyword doesn't exist")   

patients_dictionary()    #function is called