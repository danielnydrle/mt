data = [160, 223, 64, 65, 128, 126]

decoded = []

for i in range(len(data)//2):
    first = data[2*i]
    second = data[2*i + 1]
    
    ones_count = bin(first).count('1')
    parity = (8 - ones_count) % 2
    
    xor_value = first ^ (second if parity == 0 else 255 - second)
    
    if bin(xor_value).count('1') == 1:
        decoded.append(first)
    else:
        decoded.append(first ^ (255 - xor_value))

print(decoded)