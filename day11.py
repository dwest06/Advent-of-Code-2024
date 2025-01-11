init = "125 17"

init2 = "92 0 286041 8034 34394 795 8 2051489"

def read_input(init):
    return init.split(" ")

def main(init):
    blinks = [init]
    for i in range(25):
        blinks.append([])
        for j in blinks[i]:
            size = len(list(j))
            # If is 0, turn 1
            if j == '0':
                blinks[i+1].append('1')

            # if has even digits, split 
            elif size % 2 == 0:
                lj = list(j)
                half1 = ''.join(lj[:size//2])
                half2 = ''.join(lj[size//2:])
                blinks[i+1].append(str(int(half1)))
                blinks[i+1].append(str(int(half2)))

            # Else multiply by 2024
            else:
                blinks[i+1].append(str(int(j) * 2024))

    return len(blinks[-1])


def read_input_int(init):
    return list(map(int, init.split(" ")))

def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

def main2(init):

    blink = init
    for _ in range(75):
        aux = []
        for i in blink:
            size = count_digits(i)
            # If is 0, turn 1
            if i == 0:
                aux.append(1)
            # if has even digits, split 
            elif size % 2 == 0:
                half1 = i // (10 ** (size // 2))
                half2 = i % (10 ** (size // 2))
                aux.append(half1)
                aux.append(half2)

            # Else multiply by 2024
            else:
                aux.append(i * 2024)
        blink = aux.copy()
    return len(blink)

ITERS = 75
dp = [{} for _ in range(ITERS + 2)]

def calculate(num, index):

    if num in dp[index]:
        return dp[index][num]

    if index == ITERS:
        return 1

    if num == 0:
        result = calculate(1, index + 1)
        dp[index][num] = result
        return result

    size = count_digits(num)
    if size % 2 == 0:
        half1 = num // (10 ** (size // 2))
        half2 = num % (10 ** (size // 2))
        result = calculate(half1, index + 1) + calculate(half2, index + 1)
        dp[index][num] = result
        return result

    result = calculate(num * 2024, index + 1)
    dp[index][num] = result
    return result

def main3(init):
    total = 0
    for i in init:
        result = calculate(i, 0)
        total += result

    return total

# print(main(read_input(init)))

print(main3(read_input_int(init2)))