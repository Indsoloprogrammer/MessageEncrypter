from cryptography.fernet import Fernet
import base64


def encode_base64(message):
    """
    message: encrypted value
    returns the base64 value of message
    """
    base64_bytes = base64.b64encode(message)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decode_base64(encoded):
    """
    message: encoded Base64
    returns the decoded value of message
    """
    base64_bytes = encoded.encode('ascii')
    decoded = base64.b64decode(base64_bytes)
    return decoded


def generate_key():
    key = Fernet.generate_key()
    return key


def encrypt(key, message):
    """
    first encodes the message and returns the encrypted one
    """
    message = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    return encrypted


def decrypt(key, encrypted):
    """
    first decrypts the message and returns the decoded message
    """
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted.decode()


def full_encyption(key, message):
    """
    combined 2 level encryption
    """
    encrypted = encrypt(key, message)
    B64 = encode_base64(encrypted)
    return B64


def full_decryption(key, B64):
    """
    combined 2 level decryption
    """
    decoded = decode_base64(B64)
    decrypted = decrypt(key, decoded)
    return decrypted


# key = generate_key()
# print("Key: ", key)
# message = "Hello!! world..."
# encrypted = encrypt(key, message)
# B64 = encode_base64(encrypted)

# print("Message: ", message)
# print("Full encryption: ", full_encyption(key, "Hello!! world..."))
# print("Full decryption: ", full_decryption(key, B64))

# print(decrypt(b'1CVzFPZb52nwDjZfP50DvBf0jbn0QBwerd30e8JcAj8=', b'gAAAAABfuJOAP3_6QZrnwpTrZrG5zeM3BygK_6QMYeBkkVcWee2eklrgd9MKqyni9PfrsoeFnKEMD02p4WIhDGLcZAIoGGy96qyb6Y_Xhl3JOt1xkNXcz9ltGuRYxnZd389p6Ytyzmvvc3jDTPSuCXLp2AESyJtCeyqpryBGfXBj5FTZ9RUlNk4='))