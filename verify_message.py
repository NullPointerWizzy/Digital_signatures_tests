# verify_message.py
import sys
import nacl.signing
import nacl.exceptions

def verify_message(message):
    # Charger la clé publique
    with open("public_key.pem", "rb") as f:
        public_key = nacl.signing.VerifyKey(f.read())

    # Charger la signature
    with open("signature.sig", "rb") as sig_file:
        signature = sig_file.read()

    try:
        # Vérifier la signature
        public_key.verify(message.encode('utf-8'), signature)
        print("Signature valide : le message est authentique.")
        print("Message reçu : ",message)
    except nacl.exceptions.BadSignatureError:
        print("Signature invalide : le message a été falsifié.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python verify_message.py '<message>'")
        sys.exit(1)
    verify_message(sys.argv[1])
