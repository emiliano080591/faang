def a_very_big_sum(ar: [int]) -> int:
    x = 0
    for i in range(len(ar)):
        x = x + ar[i]

    return x


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    sum = a_very_big_sum(ar)
    print('La suma total es: {}'.format(sum))
