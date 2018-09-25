import sys
l = []
m = []

class MyStack(object):
    def push(char):
        m.extend(char)
        print(m)

    def pop(self):
        m.pop()
        print(m)

myst = MyStack

print("CHECKING WHETHER INPUT IS BALANCED OR NOT")
l = input("Enter enter valid string (, {, [ : ")
leng = len(l)

for x in range(leng):
    s = len(m)

    if(l[x] == '(' or l[x] == '{' or l[x] == '['):
        myst.push(l[x])

    elif (l[x] == ')'):

        if(s == 0):
            print("unbalanced")
            sys.exit()

        elif(m[s-1] == '('):
            myst.pop(None)

    elif (l[x] == ']'):

        if (s == 0):
            print("unbalanced")
            sys.exit()

        elif (m[s - 1] == '['):
            myst.pop(None)

    elif (l[x] == '}'):

        if (s == 0):
            print("unbalanced")
            sys.exit()

        elif (m[s - 1] == '{'):
            myst.pop(None)

    elif(l[x] == ')' or l[x] == '}' or l[x] == ']'):
        m.extend("a")
        break

    else:
        print("The string is balanced")

if(len(m) == 0):
    print("string balanced")
else:
    print("string unbalanced")
