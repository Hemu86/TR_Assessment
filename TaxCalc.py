#Input

name = str(input("Enter your name: "))
gender = str(input("Enter your gender(m/f): "))
age = int(input("Enter your age: "))
sal = float(input("Enter your sal: "))

# Process

if (age<=60):
    if (sal <= 250000):
        tax = 0
    elif (sal>250000 and sal<=500000):
        tax = (sal - 250000) * 0.05
    elif (sal>500000 and sal<=1000000):
        tax = (250000 * 0.05) + ((sal - 500000) * 0.2)
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + ((sal - 1000000) * 0.3)
elif (age>60 and age<=80):
    if (sal <= 300000):
        tax = 0
    elif (sal>300000 and sal<=500000):
        tax = (sal - 300000) * 0.05
    elif (sal>500000 and sal<=1000000):
        tax = (200000 * 0.05) + ((sal - 500000) * 0.2)
    else:
        tax = (200000 * 0.05) + (500000 * 0.2) + ((sal - 1000000) * 0.3)
else:
    if (sal <= 500000):
        tax = 0
    elif (sal>500000 and sal<=1000000):
        tax = (sal - 500000) * 0.2
    else:
        tax = (500000 * 0.2) + ((sal - 1000000) * 0.3)

# Output

print("Mr %s has to pay %0.2f for FY1920" %(name, tax))

    
