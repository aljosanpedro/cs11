def main():
    text = input("Text: ")
    letter_counts = histogram(text)

    count = int(input("Number of times letters appears in text: "))
    letters = reverse_lookup(letter_counts, count)

    print(f"Letters that appear {count} times in text: {letters}")



def histogram(text):
    letter_counts = {}

    for char in text:
        if char in " ,./<>?;':\"[]:\"'`~!@#$%^&*)(-=_+:":
            continue
            
        if char in letter_counts.keys():
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    return letter_counts


def reverse_lookup(letter_counts, count):
    letters = []

    for key in letter_counts.keys():
        value = letter_counts[key]

        if value == count:
            letters.append(key)

    return letters




main()
