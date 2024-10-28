import heapq

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
                counter_buffer.clear()
        return ''.join(decoded)

class HuffmanNode:
    """
    Uzel Huffmanova stromu
    """
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:
    """
    Huffmanuv enkoder/dekoder
    """
    def __init__(self, dictionary: str):
        self.dict = dictionary
        self._tree = None
        self._codes = {}

    def _build_tree(self, data: str):
        """
        Vytvoreni Huffmanova stromu
        """
        freqs = {}
        for char in data:
            freqs[char] = freqs.get(char, 0) + 1
        heap = [HuffmanNode(symbol, freq) for symbol, freq in freqs.items()]
        heapq.heapify(heap) # min-halda

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            node = HuffmanNode(None, left.freq + right.freq)
            node.left = left
            node.right = right
            heapq.heappush(heap, node)

        self._tree = heap[0]

        return heap[0]
    
    def _generate_codes(self, root: HuffmanNode, code: str = ""):
        """
        Generovani Huffmanovych kodu
        """
        if root is None:
            return
        
        if root.symbol is not None:
            self._codes[root.symbol] = code
            return
        
        self._generate_codes(root.left, code + "0")
        self._generate_codes(root.right, code + "1")

    def _serialize_tree(self):
        """
        Serializace Huffmanova stromu
        """
        def _serialize(node: HuffmanNode):
            if node is None:
                return ""
            if node.symbol is not None:
                return f"1{node.symbol}"
            return f"0{_serialize(node.left)}{_serialize(node.right)}"
        return _serialize(self._tree)
    
    def _deserialize_tree(self, data: str):
        """
        Deserializace Huffmanova stromu
        """
        if not data:
            return None, ""
        
        if data[0] == "1":
            return HuffmanNode(data[1], 0), data[2:]
        
        node = HuffmanNode(None, 0)
        left, data = self._deserialize_tree(data[1:])
        right, data = self._deserialize_tree(data)
        node.left = left
        node.right = right
        return node, data
            

    def encode(self, data: str):
        """
        Huffmanovo kodovani
        """
        if not data:
            return ""
        data = "".join(str(char) for char in data)
        self._build_tree(data)
        self._generate_codes(self._tree)
        serialized_tree = self._serialize_tree()
        encoded = "".join([self._codes[str(char)] for char in data])
        return f"{serialized_tree}|{encoded}" # oddeleni stromu a zakodovanych dat

    def decode(self, compressed_data: str):
        """
        Huffmanovo dekodovani
        """
        if not compressed_data:
            return ""
        serialized_tree, encoded = compressed_data.split("|")
        self._tree, _ = self._deserialize_tree(serialized_tree)
        decoded = []
        node = self._tree
        for char in encoded:
            if char == "0":
                node = node.left
            else:
                node = node.right
            if node.symbol is not None:
                decoded.append(node.symbol)
                node = self._tree
        return "".join(decoded)
    
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
    print(f"Dekodovana data RLE: {DECODED_RLE}")
    print_delimiter()

    print(INPUT == DECODED_RLE)
    print("\n\n")

    print("=== Huffman ===")

    huff = Huffman(SYMBOL_DICT)

    ENCODED_HUFF = huff.encode(INPUT)
    print(f"Zakodovana data Huffman: {ENCODED_HUFF}")
    print_delimiter()

    DECODED_HUFF = huff.decode(ENCODED_HUFF)
    print(f"Dekodovana data Huffman: {DECODED_HUFF}")
    print_delimiter()

    print(INPUT == DECODED_HUFF)