table = {('A','clean'):'Right',
         ('A','dirty'):'Suck',
         ('B','clean'):'Left',
         ('B','dirty'):'Suck',
        }

def main():
    while 1:
        pos = input("Enter the position of the agent ")
        stat = input("Enter status of the location ")
        action = table[(pos,stat)]

        print("Action is "+ action)

        c = input("Press Y for another input, N to exit ")

        if c == 'N':
            break


main()
