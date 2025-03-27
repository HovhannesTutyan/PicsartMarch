favorite_snacks = {
'salty': ('pretzels', 100),
'sweet': ('cookies', 180),
'veggie': ('carrots', 20),
}

for key, value in favorite_snacks.items():
    print(f"My favorite {key} food is {value[0]} that I have in quantity {value[1]}")

def bubble_sort(s):
    for i in range(len(s)):
        for j in range(1,len(s)):
            if s[j] < s[j-1]:
                s[j], s[j-1] = s[j-1], s[j]
    return s
print(bubble_sort([65,41,27,88]))


# from random import randint
# random_bits = 0
# for i in range(32):
#     if randint(0,1):
#         random_bits |= 1 << i
# print((random_bits))
print(2 << 2)