class RLE:
    """
    RLE enkoder/dekoder
    """
    def __init__(self, dictionary: str):
        self.dict = dictionary

    def encode(self, data: str):
        """
        RLE kodovani
        """
        encoded = []
        count = 1

        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append(f"{count}{chr(int(data[i - 1]) + 33)}")
                count = 1

        encoded.append(f"{count}{chr(int(data[-1]) + 33)}")
        return ''.join(encoded)

    def decode(self, compressed_data: str):
        """
        RLE dekodovani
        """
        decoded = []
        counter_buffer = []
        for char in compressed_data:
            if char.isdigit():
                counter_buffer.append(char)
            else:
                decoded.append(f"{int(ord(char) - 33)}" * int(''.join(counter_buffer)))
                counter_buffer = []
        return ''.join(decoded)

    def __str__(self):
        return f"""
        RLE kompresor
        {self}
        """

class Huffman:
    """
    Huffmanuv enkoder/dekoder
    """
    def __init__(self, dictionary: str):
        self.dict = dictionary

    def encode(self, data: str):
        pass

    def decode(self, compressed_data: str):
        pass

    def __str__(self):
        return ""
    
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
    FILE_DATA = load_file("cv06/Cv06_RLE_data.bin")
    INPUT = "".join([str(x) for x in FILE_DATA])
    SYMBOL_DICT = {str(x + 1) for x in range(0, 5)}

    print("=== RLE ===")
    print(f"Puvodni data: {INPUT}")
    print_delimiter()

    rle = RLE(SYMBOL_DICT)

    ENCODED_RLE = rle.encode(INPUT)
    print(f"Zakodovana data RLE: {ENCODED_RLE}")
    print_delimiter()

    DECODED_RLE = rle.decode(ENCODED_RLE)
    print(f"RLE dekodovana data: {DECODED_RLE}")
    print_delimiter()

    print(INPUT == DECODED_RLE)

    print("=== Huffman ===")