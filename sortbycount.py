s = 'aaaabbcaa'
i = 0
count = 1

for char in s[:-1]:
    if s[i] == s[(i + 1)]:
        count += 1
    else:
        print(s[i] + str(count), end='')
        count = 1
    i += 1
print(s[i] + str(count), end='')
