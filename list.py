marks = [25,36,98]
print(marks[-1])

print(marks[0:2])

for score in marks:
    print(score)
 
marks.append(99)
print(marks)

marks.insert(0, 99)
print(marks)

print(99 in marks)

print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.clear()
print(marks)