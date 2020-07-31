def main():
    string=input('enter a string')
    reverse(string)






def reverse(string):
    global reversed_string
    reversed_string=""
    for i in  string:
        reversed_string=i+reversed_string
    print(reversed_string )


main()