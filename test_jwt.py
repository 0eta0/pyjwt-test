import jwt
import base64

# Import key
private_key = ""
with open("./private.pem", "r") as f:
    private_key = f.read().strip()
public_key = ""
with open("./public.pem", "r") as f:
    public_key = f.read().strip()

# Generate JWT
encoded = jwt.encode({'userid': 'test'}, private_key, algorithm='ES256')
print(encoded)

# Decode JWT
decoded = jwt.decode(encoded, public_key, algorithms='ES256')
print(decoded)

# Falsify JWT
splited = encoded.split(b".")
splited[0] = base64.b64decode(splited[0].decode("utf-8"))[:-8] + b'"HS256"}'
splited[0] = base64.b64encode(splited[0])
encoded = splited[0] + b"." + splited[1] + b"." + splited[2]

# Decode falsified JWT
decoded = jwt.decode(encoded, public_key, algorithms='ES256')
print(decoded)
