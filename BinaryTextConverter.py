binary_dict = {"a": "01100001", "A": "01000001", "b": "01100010", "B": "01000010",
               "c": "01100011", "C": "01000011", "d": "01100100", "D": "01000100",
               "e": "01100101", "E": "01000101", "f": "01100110", "F": "01000110",
               "g": "01100111", "G": "01000111", "h": "01101000", "H": "01001000",
               "i": "01101001", "I": "01001001", "j": "01101010", "J": "01001010",
               "k": "01101011", "K": "01001011", "l": "01101100", "L": "01001100",
               "m": "01101101", "M": "01001101", "n": "01101110", "N": "01001110",
               "o": "01101111", "O": "01001111", "p": "01110000", "P": "01010000",
               "q": "01110001", "Q": "01010001", "r": "01110010", "R": "01010010",
               "s": "01110011", "S": "01010011", "t": "01110100", "T": "01010100",
               "u": "01110101", "U": "01010101", "v": "01110110", "V": "01010110",
               "w": "01110111", "W": "01010111", "x": "01111000", "X": "01011000",
               "y": "01111001", "Y": "01011001", "z": "01111010", "Z": "01011010",
               " ": "00100000", "?": "00111111", ".": "00101110", ",": "00101100",
               "1": "00110001", "2": "00110010", "3": "00110011", "4": "00110100",
               "5": "00110101", "6": "00110110", "7": "00110111", "8": "00111000",
               "9": "00111001", "`": "01100000", "-": "00101101", ")": "00101001",
               "=": "00111101", "!": "00100001", "@": "01000000", "#": "00100011",
               "$": "00100100", "%": "00100101", "^": "01011110", "&": "00100110",
               "*": "00101010", "(": "00101000", "[": "01011011", "]": "01011101",
               "{": "01111011", "}": "01111101", ";": "00111011", "'": "00100111",
               ":": "00111010", "<": "00111100", ">": "00111110", "/": "00101111",
               "\\": "01011100", "|": "01111100", "\"": "00100010"}


def to_binary(message):
    binary = ''
    for char in message:
        if char in binary_dict:
            binary += binary_dict[char]
    return binary


# Converts binary to text.
def from_binary(binary_message):
    message = ''
    num_chars_to_split = 8
    # converts binary into octets for comparing to dictionary
    split_message = [(binary_message[i:i+num_chars_to_split])
                     for i in range(0, len(binary_message), num_chars_to_split)]
    for code in split_message:
        for char, binary in binary_dict.items():
            if binary == code:
                message += char
    return message


# Driver code
def main():
    while True:
        choice = input(
            "Choose an option:\nPress 1 to convert text to Binary\nPress 2 to convert Binary to text\nPress -1 to quit\n: ")
        if choice == '1':
            message = input("Enter a message to convert to Binary: ")
            binary = to_binary(message)
            print(f"Your encoded message is : {binary}")

        elif choice == '2':
            binary_message = input(
                "Enter a Binary sequence to convert to text: ")
            message = from_binary(binary_message)
            print(f"Your decoded message is : {message}")

        elif choice == '-1':
            print("Session Closed")
            break

        else:
            print("Invalid choice, please choose from the available options.")


if __name__ == "__main__":
    main()