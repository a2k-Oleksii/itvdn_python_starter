aabbaa = list('aabbbaa')
first_half = aabbaa[0:int(aabbaa.__len__()/2)]
second_half = aabbaa[int(aabbaa.__len__()/2): int(aabbaa.__len__())]
second_half.reverse()
x = 0
marker = True

while x < first_half.__len__():
    if first_half[x] == second_half[x]:
        pass
    else:
        marker = False
    x += 1

if marker:
    print("This is word palindrome")
else:
    print("This is word not palindrome")
