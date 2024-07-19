import sys
string_list= []
for i in range(3) :
    string_list.append(sys.stdin.readline().rstrip())
for i in range(len(string_list)) :
    if string_list[i].isdigit() :
        num = int(string_list[i])
        idx = i
next_int = num + (3-idx)

if next_int % 3 == 0:
    if next_int % 5 == 0 :
        print('FizzBuzz')
    else :
        print('Fizz')
elif next_int % 5 == 0 :
    print("Buzz")
else :
    print(next_int)
