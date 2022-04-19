import os

input_variable = os.environ['INPUT_STORE']

def main():
    with open('readme.txt', 'w') as f:
        f.write(input_variable)
    print(input_variable)

main()