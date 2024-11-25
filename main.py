from cryptography.fernet import Fernet

# Кілтті генерациялау
key = Fernet.generate_key()
cipher = Fernet(key)

# Кілтті файлға жазу
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Шифрланатын хабар
khat = b"salem, kalaisyn?"
korgalgan_khat = cipher.encrypt(khat)

print(korgalgan_khat)

# Шифрланған хабарды файлға жазу
with open("Khat.txt", "wb") as file:
    file.write(korgalgan_khat)
