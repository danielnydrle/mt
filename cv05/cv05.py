DICT = [str(x) for x in range(1, 6)]

def compress_lzw(raw_data: str) -> str:
    result = []
    current = ""
    for char in raw_data:
        if current + char in DICT:
            current += char
        else:
            result.append(DICT.index(current))
            DICT.append(current + char)
            current = char
    if current:
        result.append(DICT.index(current))
    print(f"Dictionary: {DICT}, {len(DICT)}")
    print(f"Compressed (indices): {result}")
    compressed = "".join([chr(x + 33) for x in result])  # Převod na tisknutelné ASCII znaky
    print(f"Compressed (ASCII): {compressed}")
    return compressed


def decompress_lzw(compressed_data: str) -> str:
    result = []
    DICT_decompression = DICT.copy()  # Vytvoříme kopii slovníku pro dekompresi
    prev = compressed_data[0]
    result.append(DICT_decompression[ord(prev) - 33])
    for char in compressed_data[1:]:
        code = ord(char) - 33
        if code < len(DICT_decompression):
            entry = DICT_decompression[code]
        elif code == len(DICT_decompression):
            entry = result[-1] + result[-1][0]
        else:
            raise ValueError(f"Invalid compressed data: {code}")
        
        result.append(entry)
        DICT_decompression.append(result[-2] + entry[0])
        prev = char
    return "".join(result)


def load_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

if __name__ == "__main__":
    data = load_file("cv05/Cv05_LZW_data.bin")
    input = "".join([str(x) for x in data])

    print(input)
    compressed = compress_lzw(input)
    print(compressed)
    decompressed = decompress_lzw(compressed)
    print(decompressed)
    print(input == decompressed)