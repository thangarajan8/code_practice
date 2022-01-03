#https://leetcode.com/problems/roman-to-integer/
roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
roman_word = 'MCMXCIV'
roman_word ='III'
prev= 0
next_ = 0
total = 0
mixed_flag = False
#for i in range(len(roman_word)-1):
#    print(i,i+1)
#    l = roman_word[i]
#    r = roman_word[i+1]
#    left = roman_dict[l]
#    right = roman_dict[r]
#    if left <= right:
#        print(('mixed'),(l,r),(left,right), right-left)
#        total += right-left
#        mixed_flag = True
#        i += 1
#    elif not mixed_flag:
#        print(('stright'),l,left)
#        total += left
#    else:
#        print(left)        

t1 = 0
prev = 0
nex = 0
for i in range(len(roman_word)):
    print(i)
    l = roman_word[i]
    left = roman_dict[l]
    total
