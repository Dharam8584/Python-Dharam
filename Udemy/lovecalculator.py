yourName = str(input("please enter your name: "))
loverName =str(input("please enter the lovers name; "))
combined_name = yourName + loverName
lc_combined_name = combined_name.lower()
print(lc_combined_name)

t = lc_combined_name.count('t')
r = lc_combined_name.count('r')
u = lc_combined_name.count('u')
e = lc_combined_name.count('e')

true = t + r + u + e

l = lc_combined_name.count('l')
o = lc_combined_name.count('o')
v = lc_combined_name.count('v') 
e = lc_combined_name.count('e')

love = l + o + v + e

love_score = str(true) + str(love)
print('YOur Love percentage is '+ love_score)
