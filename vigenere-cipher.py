def vigenere_cipher_decode(encoded_message, keyword):
    encoded_words = encoded_message.split()
    decoded_words = []
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,!?' "
    
    counter = 0
    for word in encoded_words:
        decoded_letters = []
        for character in word:
            if character in punctuation:
                decoded_letters.append(character)
            else:
                keyword_index = counter % len(keyword)
                offset = alphabet.find(keyword[keyword_index])
                index = (alphabet.find(character) + offset) % 26
                decoded_letters.append(alphabet[index])
                counter += 1
        
        decoded_words.append("".join(decoded_letters))
    
    decoded_message = " ".join(decoded_words)
    return decoded_message

encoded_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
print(vigenere_cipher_decode(encoded_message, "friends"))

def vigenere_cipher_encode(message, keyword):
    message_words = message.split()
    encoded_words = []
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,!?' "
    
    counter = 0
    for word in message_words:
        encoded_letters = []
        for character in word:
            if character in punctuation:
                encoded_letters.append(character)
            else:
                keyword_index = counter % len(keyword)
                offset = alphabet.find(keyword[keyword_index])
                index = (alphabet.find(character) - offset)
                encoded_letters.append(alphabet[index])
                counter += 1
        
        encoded_words.append("".join(encoded_letters))
    
    encoded_message = " ".join(encoded_words)
    return encoded_message

message = "you were able to decode this? nice work! you are becoming quite the expert at cryptography!"
print(vigenere_cipher_encode(message, "friends"))
