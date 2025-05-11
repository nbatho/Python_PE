def read_words(filename):
    words = set()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words.update(line.strip().lower().split())
    return words
a = read_words('DATA1.in')
b = read_words('DATA2.in')

only_in_a = sorted(a - b)
only_in_b = sorted(b - a)

print(" ".join(only_in_a))
print(" ".join(only_in_b))
