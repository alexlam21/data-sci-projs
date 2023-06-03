def caesar_decode(encoded_message, offset):
    encoded_words = encoded_message.split()
    decoded_words = []
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,!? "
    
    for word in encoded_words:
        decoded_letters = []
        for letter in word:
            if letter in punctuation:
                decoded_letters.append(letter)
            else:
                index = alphabet.find(letter)
                index = (index + offset) % 26
                decoded_letters.append(alphabet[index])
                
        decoded_words.append("".join(decoded_letters))
                
    decoded_message = " ".join(decoded_words)
    return decoded_message

def caesar_encode(message, offset):
    message_words = message.split()
    encoded_words = []
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,!? "
    
    for word in message_words:
        encoded_letters = []
        for letter in word:
            if letter in punctuation:
                encoded_letters.append(letter)
            else:
                index = alphabet.find(letter)
                index = index - offset
                encoded_letters.append(alphabet[index])
                
        encoded_words.append("".join(encoded_letters))
    
    encoded_message = " ".join(encoded_words)
    return encoded_message

encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(caesar_decode(encoded_message, 10))
message = """this is an example of a caesar cipher."""

print(caesar_encode("hey there! i got your message. here is mine."))
print(caesar_encode(message, 10))

message = """this is 
an example of a caesar 
            cipher.hey there"""

print(caesar_encode("hey there! i got your message. here is mine.",10))
print(caesar_encode(message,14))
