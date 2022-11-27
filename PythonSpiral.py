#PythonSpiral.py
#Connor Garrick
#November 27, 2022

#Enter a message in console and create a word pyramid
if __name__ == '__main__':
    print("This program prints a word pyramid from a given prompt. Please enter a string below, type \"default\" to print a word pyramid of \"Hello World\", or type \"exit\" to exit.")
    inp = "empty"

    while inp != "exit":
        inp = input('Enter your string here: ')

        if inp == "exit":
            break

        if inp == 'default':
            inp = "Hello World"
            for n in range(len(inp)):
                for m in range(n + 1):
                    print(inp[m], end="")
                print()
        else:
            for n in range(len(inp)):
                for m in range(n + 1):
                    print(inp[m], end="")
                print()