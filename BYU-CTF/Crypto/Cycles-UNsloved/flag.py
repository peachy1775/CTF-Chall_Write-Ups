from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

p = 121407847840823587654648673057258513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289381
g = 3
ct = b"S\x00\xe7%\xcd\xec\xad\x9a\xe1lO\x80\xd6\r\xa5\x00\x19Y\x18\x7f\xa1\x9cx\x98\xb08n~-\rj2\xd4d\xd2\xda\xa6\xd0\r#7\xee-\\\xb4\x10\x98\x8f"
hint = 1  # from your original output


def try_key(a):
    key = long_to_bytes(a)[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = unpad(cipher.decrypt(ct), AES.block_size)
        print(f"[+] Found a = {a}")
        print("[+] Flag:", plaintext.decode())
        return True
    except:
        return False


print("[*] Starting brute force for a...")

# Since hint = 1 means pow(g,a,p) = 1,
# 'a' is likely multiple of order of g, try multiples of 1 up to a range
for a_candidate in range(1, 1000000):
    if pow(g, a_candidate, p) == hint:
        if try_key(a_candidate):
            break
