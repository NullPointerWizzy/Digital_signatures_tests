# key_gen.py
import nacl.signing
import nacl.encoding

def generate_keys():
    # Générer une clé privée Ed25519
    private_key = nacl.signing.SigningKey.generate()
    public_key = private_key.verify_key

    # Sauvegarder la clé privée
    with open("private_key.pem", "wb") as f:
        f.write(private_key.encode(encoder=nacl.encoding.RawEncoder()))

    # Sauvegarder la clé publique
    with open("public_key.pem", "wb") as f:
        f.write(public_key.encode(encoder=nacl.encoding.RawEncoder()))

    print("Clés générées et sauvegardées dans 'private_key.pem' et 'public_key.pem'.")

if __name__ == "__main__":
    generate_keys()
