def lbs_to_kg(weight):
    return int(weight) * .45

def kg_to_lbs(weight):
    return int(weight) / .45

print((kg_to_lbs(input("Enter your weight in pounds: "))))
print((lbs_to_kg(input("Enter your weight in pounds: "))))