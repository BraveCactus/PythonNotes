# from functools import reduce
# volume = reduce(lambda x, y: x * y, map(int, input().strip().split()))
# print(f"{volume}")

names = ["Аурелиано", "Ремедиос", "Пьетро", "Аркадио", "Урсула"]
names_starts_a_1 = [name for name in names if name.startswith("А")]
print(names_starts_a_1)

names = ["Аурелиано", "Ремедиос", "Пьетро", "Аркадио", "Урсула"]
names_starts_a_2 = list(filter(lambda name: name.startswith("А"), names))
print(names_starts_a_2)

if (all(name.startswith("А") for name in names)):
    print("Все имена начинаются с А")
elif (any(name.startswith("А") for name in names)):
    print("Какие-то имена начинаются с А")

result = True if all(name.startswith("А") for name in names) else False
print(result)