first = [1, 2, 3, 4, 5, 6]
bonus = 7
my = [1, 2, 3, 4, 5, 7,]


bou = 0
same = 0
for i in my:
    if i in first:
        same += 1
    elif i == bonus:
        bou = 1

result = '꽝'
if same == 6 and bou == 0:
    result = 1
elif same == 5 and bou == 1:
    result = 2
elif same == 5 and bou == 0:
    result = 3
elif same == 4:
    result = 4
elif same == 3:
    result = 5

return render_template(

)
