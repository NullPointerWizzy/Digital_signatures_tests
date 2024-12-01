# sign_message.py
import sys
import nacl.signing

def sign_message(message):
    # Charger la clé privée
    with open("private_key.pem", "rb") as f:
        private_key = nacl.signing.SigningKey(f.read())

    # Signer le message
    signed_message = private_key.sign(message.encode('utf-8'))

    # Sauvegarder la signature
    with open("signature.sig", "wb") as sig_file:
        sig_file.write(signed_message.signature)

    print(f"Message signé avec succès. Signature sauvegardée dans 'signature.sig'.")
    print(f"Signature (hex) : {signed_message.signature.hex()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python sign_message.py '<message>'")
        sys.exit(1)
    sign_message(sys.argv[1])
