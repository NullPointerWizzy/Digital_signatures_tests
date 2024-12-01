#!/bin/bash

# Vérification des paramètres
if [ $# -eq 0 ]; then
  echo "Erreur : aucun message fourni."
  echo "Usage : ./test_communication.sh '<message>'"
  exit 1
fi

# Récupération du message complet
MESSAGE="$*"

# Vérification de la taille du message (UTF-8)
BYTE_SIZE=$(echo -n "$MESSAGE" | wc -c)

if [ "$BYTE_SIZE" -gt 186 ]; then
  echo "Erreur : le message dépasse 186 octets ($BYTE_SIZE octets fournis)."
  exit 1
fi

# Générer les clés
echo "[1/4] Génération des clés..."
python3 key_gen.py

# Signer le message
echo "[2/4] Signature du message : '$MESSAGE'..."
python3 sign_message.py "$MESSAGE"

# Vérifier la signature
echo "[3/4] Vérification de la signature..."
python3 verify_message.py "$MESSAGE"

# Test avec un message modifié (attaque simulée)
FAKE_MESSAGE="Message falsifié."
echo "[4/4] Tentative de vérification d'un message falsifié : '$FAKE_MESSAGE'..."
python3 verify_message.py "$FAKE_MESSAGE"
