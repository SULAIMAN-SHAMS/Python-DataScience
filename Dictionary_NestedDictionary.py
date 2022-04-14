
# DICTIONARIES  by SULAIMAN SHAMS

student1={'SULAIMAN SHAMS':{'Age':'25', 'Marks':'80%'},'HARIS ALI':{'Age':'25', 'Marks':'80%'}}
print(student1)

print("SULAIMAN SHAMS")
print(student1['SULAIMAN SHAMS'])

print("HARIS ALI")
print(student1['HARIS ALI'])

print(student1.keys())

print("This is nested dictionary")
student2={1:{'SULAIMAN SHAMS':{'Age':'25', 'Marks':'80%'}},2:{'HARIS ALI':{'Age':'25', 'Marks':'80%'}}}
print(student2)

print("ShoW haris Ali data by key 2")
print(student2[2])
print("Age of Haris ALI?")
print(student2[2]['HARIS ALI']['Age'])
