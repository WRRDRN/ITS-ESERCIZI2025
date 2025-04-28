
#!/usr/bin/env python3

def trasforma_byte(b, k, posizione):
    rotazione = (k + posizione) % 8
    b_rotato = ((b >> rotazione) | (b << (8 - rotazione))) & 0xFF
    chiave_modificata = (k ^ posizione) & 0xFF
    return b_rotato ^ chiave_modificata

def inverse_trasforma_byte(b_criptato, k, posizione):
    for candidate in range(256):
        if trasforma_byte(candidate, k, posizione) == b_criptato:
            return candidate
    return None

def decrypt(cipher_bytes, chiave_numerica):
    chiave = [((chiave_numerica >> (i * 8)) & 0xFF) for i in range(8)]
    output = bytearray()
    for i, b in enumerate(cipher_bytes):
        k = chiave[i % 8]
        plain_byte = inverse_trasforma_byte(b, k, i)
        if plain_byte is None:
            return None
        output.append(plain_byte)
    return output

def invert_xor_cumulativa(data):
    plain = bytearray(len(data))
    plain[0] = data[0]
    for i in range(1, len(data)):
        plain[i] = data[i] ^ data[i - 1]
    return plain

def main():
    hex_data = "de 14 81 00 ab 1e 99 4d 8d 46 d4 4e f3 62 bd 7b e0 09 89 16 a0 19 cf 18 e7 35 b8 19 a2 09 91 70 8b 3d 8d 2a a7"
    cipher = bytearray(int(b, 16) for b in hex_data.split())
    xor_inverted = invert_xor_cumulativa(cipher)

    for key in range(0x100000):
        result = decrypt(xor_inverted, key)
        if result:
            try:
                output = result.decode('utf-8')
                if "flag{" in output:
                    print(f"[+] Chiave trovata: {hex(key)}")
                    print(f"[+] Messaggio decifrato: {output}")
                    break
            except UnicodeDecodeError:
                continue

if __name__ == "__main__":
    main()