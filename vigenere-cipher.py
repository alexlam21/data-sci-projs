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
