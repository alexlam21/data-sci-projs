def caesar_decode(encoded_message):
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
                index = (index + 10) % 26
                decoded_letters.append(alphabet[index])
                
        decoded_words.append("".join(decoded_letters))
                
    decoded_message = " ".join(decoded_words)
    return decoded_message

encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

print(caesar_decode(encoded_message))
