def get_longest_div_k(lst, k):
        """
        determina cea mai lunga subsecv care este div cu k
        """
        max_div_k = div_k = start = end = 0
        for i in range(len(lst)):
            if lst[i] % k == 0:
                div_k+=1
                if max_div_k < div_k:
                    max_div_k = div_k
                    start = i - div_k + 1
                    end = i
            else:
                div_k = 0
        
        while start <= end:
            print(lst[start])
            start += 1

def prime_digits(n):
    """
    determina daca numarul e format din cifre prime
    """
    ok = 1
    copy = n
    while copy != 0:
        c = copy % 10
        if c == 1 or c == 4 or c == 6 or c == 8 or c == 9: 
            ok = 0
        copy = copy//10

    if ok == 0:
        return 0
    return 1


def get_longest_prime_digits(lst):
    """
    determina cea mai lunga subsecv de numere formate din cifre prime
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i, l):
            k = prime_digits(lst[i])
            all_prime_digits = True
            for num in lst[i:j + 1]:
                if prime_digits(num) != k :
                    all_prime_digits = False
                    break
            if all_prime_digits:
                if j - i + 1 >len(result):
                    result = lst[i:j + 1]
    return result


def read_array(lst, length):
    print("Introduceti numerele sirului: ")
    for i in range(length):
        lst.append(int(input()))

def read_statements():
    problem = input("Introduceti numarul problemei: ")
    length = int(input("Introduceti lungimea sirului: "))
    lst = []
    if problem == "1":
        read_array(lst, length)
        print(get_longest_prime_digits(lst))
    elif problem == "2":
        k = int(input("Elementul K: "))
        read_array(lst, length)
        get_longest_div_k(lst, k)

def main():
    print("1. Sa se determine cea mai lunga subsecventa care are toate numerele formate din cifre prime.")
    print("2. Sa se determine cea mai lunga subseceventa divizibila cu k.")
    read_statements()

if __name__ == '__main__':
    main()