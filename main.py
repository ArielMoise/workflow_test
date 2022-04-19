#main

def main():
    user_input = input('write some random test: ')

    with open('readme.txt', 'w') as f:
        f.write(user_input)


main()