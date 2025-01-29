
print("Input text: ")
text1 = input()
print("Input text to find: ")
textToFind1 = input()

test(text1, textToFind1)


def test(text, textToFind):
    length = len(textToFind)
    current = 0
    for char in text:
        if char == textToFind[current]:
            current += 1
            if current == length:
                return True
            
    return False