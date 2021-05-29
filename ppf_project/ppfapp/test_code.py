'''


def temp_fun(s):
    zero_count = 1
    for i in range(l):
        if s[i].isdigit():
            if zero_count < z_count:
                for j in range(l - 1, -1, -1):
                    if s[j].isalpha():
                        temp = s[i]
                        s[i] = s[j]
                        s[j] = temp
                        break
                zero_count = zero_count + 1
    return s


if __name__ == "__main__":
    input = "fw0fs0bta0"
    z_count = input.count('0')      # count zeros from string
    s = list(input)                 # convert string to list
    l = len(s)
    output = temp_fun(s)

    output = ''.join(map(str, s))
    print("final output:", output)

'''



def countSubarray(arr, n, k):
    count = 0

    for i in range(0, n):
        sum = 0;
        for j in range(i, n):
            if (sum + arr[j] <= k):
                sum = arr[j] + sum

                print("sum::",sum)
                print(arr[i:j+1])
                count += 1
            else:
                break


if __name__ == "__main__":
    array = [1, 2, 3]
    k = 5
    size = len(array)
    countSubarray(array, size, k);


