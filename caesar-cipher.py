alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = "".join(alphabet)
punctuation = ".,!? "
string = "xhello"

# for letter in string:
#   print(t.find(letter))
# print("." in punctuation)

encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

encoded_words = encoded_message.split()
# print(encoded_words)
decoded_words = []

def caesar_decode(message):
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
# print(decoded_words)

decoded_message = " ".join(decoded_words)
print(decoded_message)
