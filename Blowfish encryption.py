from Crypto.Cipher import Blowfish
cipher = Blowfish.new("key must be 4 to 56 bytes")
# input data must multiple of 8
data = input("Enter the data that need to encrypt: ")
encrypted_data = cipher.encrypt(data)
print("The encrypted message is: ", encrypted_data)