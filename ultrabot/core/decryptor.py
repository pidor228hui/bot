import os

from cryptography.fernet import Fernet, InvalidToken


def decrypt_tokens(enc_path: str, master_key: str) -> list[str]:
    if not master_key:
        raise RuntimeError("MASTER_KEY is not set")
    if not os.path.exists(enc_path):
        raise FileNotFoundError(f"Encrypted tokens file not found: {enc_path}")

    with open(enc_path, "rb") as encrypted_file:
        encrypted = encrypted_file.read().strip()

    try:
        decrypted = Fernet(master_key).decrypt(encrypted)
    except InvalidToken as exc:
        raise RuntimeError("Failed to decrypt tokens.enc: invalid MASTER_KEY") from exc

    return [line.strip() for line in decrypted.decode("utf-8").splitlines() if line.strip()]
