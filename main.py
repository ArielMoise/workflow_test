import os

input_variable = os.environ['INPUT']

def main():
    with open('readme.txt', 'w') as f:
        f.write(input_variable)

main()
print("input_variable")
print(input_variable)