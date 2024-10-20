"""
Daniel Nydrle
Cv05 - LZW
"""

class LZW:
    """
    LZW kompresor/dekompresor
    """
    def __init__(self, data: str, dictionary: str):
        self.data = data
        self.dict = dictionary

    def compress(self):
        """
        LZW komprese
        """
        res = []
        phrase = ""
        for char in self.data:
            if f"{phrase}{char}" in self.dict:
                phrase += char
            else:
                res.append(self.dict.index(phrase))
                self.dict.append(f"{phrase}{char}")
                phrase = char
        if phrase: # zbytek
            res.append(self.dict.index(phrase))
        compressed = "".join([chr(x + 33) for x in res]) # ASCII translace (neni potreba, pouze pro zobrazeni v konzoli)
        return compressed
    
    def decompress(self, compressed_data):
        """
        LZW dekomprese
        """
        res = []
        prev = compressed_data[0]
        res.append(self.dict[ord(prev) - 33])
        for char in compressed_data[1:]:
            code = ord(char) - 33
            entry = self.dict[code] if code < len(self.dict) else f"{res[-1]}{res[-1][0]}"
            res.append(entry)
            self.dict.append(f"{res[-2]}{entry[0]}")
            prev = char
        res = "".join(res)
        return res


def load_file(file_path):
    """
    Nacteni binarniho souboru
    """
    with open(file_path, "rb") as file:
        return file.read()
    
def print_delimiter():
    """
    Vypsani oddelovace
    """
    print("=" * 50)

if __name__ == "__main__":
    FILE_DATA = load_file("cv05/Cv05_LZW_data.bin")
    INPUT = "".join([str(x) for x in FILE_DATA])
    SYMBOL_DICT = [str(x) for x in range(1, 6)]
    
    print(f"Puvodni data: {INPUT}")
    print_delimiter()

    LZW = LZW(INPUT, SYMBOL_DICT)

    COMPRESSED = LZW.compress()
    print(f"Kompresovana data (s ASCII translaci): {COMPRESSED}")
    print_delimiter()

    DECOMPRESSED = LZW.decompress(COMPRESSED)
    print(f"Dekompresovana data: {DECOMPRESSED}")
    print_delimiter()

    print(INPUT == DECOMPRESSED)