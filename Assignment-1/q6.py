StringList1 = input('Enter List of Strings : ').split()

MStringList1 = []

for e in StringList1:
    if StringList1.count(e) >= 2:
        MStringList1.append(e)

for item in MStringList1:
    if StringList1.count(item) % 2 == 0:
        print(item, "occurs an even number of times in StringList1")
    else:
        print(item, "occurs an odd number of times in StringList1")


word = input('Enter word for removing...')
count = 0
for i in range(len(StringList1)):
    if StringList1[i] == word:
        count += 1
        if count >= 2:
            del StringList1[i]
            break

print("Modified StringList1:", StringList1)