import math


class Arithmetic:
    """
    Aritmeticky enkoder/dekoder
    """

    def __init__(self, dictionary: dict):
        self.dict = dictionary
        counts = {}
        for char in dictionary:
            counts[char] = counts.get(char, 0) + 1

        self.probs = {}
        self.ranges = {}

        curr = 0.0

        for char, count in counts.items():
            prob = count / len(dictionary)
            self.probs[char] = prob
            self.ranges[char] = (curr, curr + prob)
            curr += prob

    def encode(self, data: str):
        """
        Aritmeticke kodovani
        """
        l = 0.0
        h = 1.0

        for char in data:
            char_range = h - l
            char_low, char_high = self.ranges[char]
            h = l + char_range * char_high
            l = l + char_range * char_low
            
        res = (l + h) / 2 + len(data)
        
        return str(res)
            

    def decode(self, compressed_data: str):
        """
        Aritmeticke dekodovani
        """
        c = float(compressed_data)
        data_length = int(c)
        c = c - data_length
        res = []
        k = c

        for _ in range(data_length):
            for char, (l, h) in self.ranges.items():
                if l <= k < h:
                    res.append(char)
                    k = (k - l) / (h - l)
                    break

        return "".join(res)

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
    FILE_DATA = load_file("cv07/Cv07_Aritm_data.bin")
    INPUT = "".join([str(x) for x in FILE_DATA])

    print(f"Puvodni data: {INPUT}")
    print_delimiter()

    SYMBOL_DICT = {str(x + 1) for x in range(0, 5)}

    arithm = Arithmetic(SYMBOL_DICT)
    ENCODED = arithm.encode(INPUT)
    print(f"Zakodovana data: {ENCODED}")
    print_delimiter()

    DECODED = arithm.decode(ENCODED)
    print(f"Dekodovana data: {DECODED}")
    print_delimiter()

    print(INPUT == DECODED)