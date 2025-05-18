from math import isqrt
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

pem_key = b"""-----BEGIN PUBLIC KEY-----
MIIBAjANBgkqhkiG9w0BAQEFAAOB8AAwgewCgeQo+PHTOEh57OGg5PqZD97ln4O8
z1/EHSeDplfjytTxgfChwrf2Hg85G3sRr8UCsHDlVaOcFNmz6ubInjMOD2j7d4kk
OOk+bBzJSGnOgFJbWdCXwMeDFhoUjVNw/UreHmX0kGCni9ci4PpO1iTzdHpNYZAS
L9G3eMpbu9hcoEyuE+GXvlJ11MWBGiot8YbjdK1fixH29QHDLNqmrBFwd5Y5XCqV
e1xzmEAcm5vgbBjduXmBxevx7OdWT0K4RDcFBqC8nfwq5UZJqwXvSDmB59fs1tbb
uqzcToCcxUr6xM4wiUPHxeECAwEAAQ==
-----END PUBLIC KEY-----"""

key = RSA.import_key(pem_key)
N = key.n

flag_candidate = isqrt(N)

flag = long_to_bytes(flag_candidate)
print(f"[+] Flag candidate (bytes): {flag}")
print(f"[+] Flag candidate (utf-8): {flag.decode(errors='ignore')}")
