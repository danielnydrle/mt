ENGLISH_IOC = 0.06689
CZECH_IOC = 0.06027


def calculate_ioc(text):
    text = ''.join(c for c in text.upper() if c.isalpha())
    n = len(text)
    if n < 2:
        return 0

    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    ioc = 0
    for count in freq.values():
        ioc += count * (count - 1)

    ioc = ioc / (n * (n - 1))
    return ioc


def identify_language(text):
    ioc = calculate_ioc(text)

    if abs(ioc - ENGLISH_IOC) < abs(ioc - CZECH_IOC):
        return "English", ioc
    else:
        return "Czech", ioc


def caesar_decrypt(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for shift in range(26):
        decrypted = ""
        for c in text.upper():
            if c in alphabet:
                pos = alphabet.index(c)
                new_pos = (pos - shift) % 26
                decrypted += alphabet[new_pos]
            else:
                decrypted += c
        yield decrypted


def identify_language_and_decrypt():
    with open('cv15/cv14_text01.txt', 'r', encoding='utf-8') as file:
        text1 = file.read().strip()
    with open('cv15/cv14_text02.txt', 'r', encoding='utf-8') as file:
        text2 = file.read().strip()

    # reverse the texts
    text1 = text1[::-1]
    text2 = text2[::-1]

    for text_num, text in enumerate([text1, text2], 1):
        print(f"\nAnalyzing text {text_num}: {text[:50]}...")
        language, ioc = identify_language(text)
        print(f"Language identified: {language}")
        print(f"Index of Coincidence: {ioc:.4f}")

        print("\nDecrypted text:")
        key = "ROADS" if language == "English" else "DOMOV"
        for decrypted in caesar_decrypt(text):
            if key in decrypted:
                print(f"Key: {key}")
                print(decrypted)


if __name__ == "__main__":
    identify_language_and_decrypt()
