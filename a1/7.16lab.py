def output_without_whitespace(input_str):
    print("String with no whitespace: {}".format(input_str.replace(" ", "")))

def get_num_of_characters(input_str):
    counter = 0
    for i in input_str:
        counter = counter + 1
    print("Number of characters: {}".format(str(counter)))


if __name__ == '__main__':
    input_str = input("Enter a sentence or phrase:")
    print()
    print()
    print("You entered: {}".format(input_str))
    print()
    get_num_of_characters(input_str)
    output_without_whitespace(input_str)

