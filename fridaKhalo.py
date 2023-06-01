paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]
paintings = list(zip(paintings, dates))
print(paintings)

paintings += [("The Broken Column", 1944),("The Wounded Deer", 1946),("Me and My Doll" , 1937)]


print(len(paintings))
print(paintings)

audio_tour_number = [i + 1 for i in range(7)]

master_list = list(zip(audio_tour_number, paintings))
print(master_list)
