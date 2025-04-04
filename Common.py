def encode(text):
    from base64 import b64encode
    return b64encode(bytes(text, encoding='utf-8'))


def decode(byte_str):
    from base64 import b64decode
    return b64decode(byte_str).decode('utf-8')

