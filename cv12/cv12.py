# 1: binarni kod do Grayova kodu
def binary2gray(binary):
    gray = binary[0]
    for i in range(1, len(binary)):
        gray += str((int(binary[i]) + int(binary[i - 1])) % 2)
    return gray

def show_conversion_table():
    print("Binary -> Gray")
    for i in range(16):
        binary = format(i, "04b")
        print(f"{binary} -> {binary2gray(binary)}")

show_conversion_table()


# 2: Move-To-Front algoritmus
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def mtf_encode(text, alphabet=ALPHABET):
    current_alphabet = list(alphabet)
    result = []
    
    for char in text:
        position = current_alphabet.index(char) + 1
        result.append(position)
        
        char_to_move = current_alphabet.pop(position - 1)
        current_alphabet.insert(0, char_to_move)
    
    return result

def mtf_decode(encoded, alphabet=ALPHABET):
    current_alphabet = list(alphabet)
    decoded = []
    
    for pos in encoded:
        char = current_alphabet[pos - 1]
        decoded.append(char)
        
        char_to_move = current_alphabet.pop(pos - 1)
        current_alphabet.insert(0, char_to_move)
    
    return ''.join(decoded)

def test_mtf():
    print("MTF")
    text = input().upper()
    encoded = mtf_encode(text)
    print(f"Encoded: {encoded}")
    decoded = mtf_decode(encoded)
    print(f"Decoded: {decoded}")

test_mtf()

# 3: Burrows-Wheelerova transformace
def bwt_encode(text):
    n = len(text)

    rotations = [text[i:] + text[:i] for i in range(n)]
    rotations.sort()

    bwt_result = ''.join(row[-1] for row in rotations)
    original_index = rotations.index(text)
    return bwt_result, original_index
 
def bwt_decode(encoded_string, original_index):
    n = len(encoded_string)

    table = [""] * n

    for _ in range(n):
        table = sorted([encoded_string[i] + table[i] for i in range(n)])

    original_string = table[original_index]
    return original_string

def test_bwt():
    print("BWT")
    input_string = input().upper()
    encoded, original_index = bwt_encode(input_string)
    print(f"Encoded: {encoded}")
    decoded = bwt_decode(encoded, original_index)
    print(f"Decoded: {decoded}")

test_bwt()
