import random
primes = []

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

for i in range(1000, 10000):
    if is_prime(i):
        primes.append(i)

class RSA:
    def __init__(self):
        p = primes[random.randint(0, len(primes)-1)]
        q = primes[random.randint(0, len(primes)-1)]
        n = p * q
        phi = (p-1) * (q-1)
        e = 0
        for i in range(2, phi):
            if is_prime(i) and phi % i != 0:
                e = i
                break
        d = 0
        while True:
            if (d * e) % phi == 1:
                break
            d += 1
        self.public_key = (n, e)
        self.private_key = (n, d)

    def encrypt(self, text: str):
        encrypted = []
        for char in text:
            encrypted.append(pow(ord(char), self.public_key[1], self.public_key[0]))
        return encrypted
    
    def decrypt(self, encrypted: list):
        decrypted = []
        for char in encrypted:
            decrypted.append(chr(pow(char, self.private_key[1], self.private_key[0])))
        return "".join(decrypted)
    
    def __str__(self):
        return f"Public key: {self.public_key}\nPrivate key: {self.private_key}"

rsa = RSA()
print(rsa)
text = input("Vloz text: ")
encrypted = rsa.encrypt(text)
print(encrypted)
decrypted = rsa.decrypt(encrypted)
print(decrypted)