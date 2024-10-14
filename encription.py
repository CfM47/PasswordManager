import random

def gen_random_password():
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+|;:,.<>?/"
  n = random.randint(10, 20)
  password = ""
  alph = len(chars)
  for i in range(n):
    k = random.randint(0, 2**32)
    password += chars[k % alph]
  return password
  
def get_numeric_key(s):
    key = 0
    for i, c in enumerate(s):
      key += ord(c) * (256 ** i)
    return key % (2**64)

def encript_str(s, key):
  encripted_str = ""
  random.seed(abs(key))
  for c in s:
    offset = random.getrandbits(64) % 256
    mod_c = ord(c) % 256
    new_c = (mod_c + offset) % 256
    encripted_str += chr(new_c)
  return encripted_str

def decript_str(s, key):
  decripted_str = ""
  random.seed(key)
  for c in s:
    offset = random.getrandbits(64) % 256
    mod_c = ord(c) % 256
    new_c = (mod_c - offset + 256) % 256
    decripted_str += chr(new_c)
  return decripted_str