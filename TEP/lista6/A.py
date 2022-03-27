#S is a string of length 3 if a caracter is S is sunny and R is rainny
S = input()

#Check for the most consecutive rainny days
max = 0
max_s = 0

for s in S:
    if s == "R":
        max += 1
        if max > 0:
            max_s = max
    else:
        max = 0
print(max_s)
