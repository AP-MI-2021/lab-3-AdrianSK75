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

def is_palindrome(n):
    copie = n
    invers = 0
    while copie != 0:
        cifra = copie % 10
        invers = invers * 10 + cifra
        copie = copie//10

    if invers == n:
        return 1
    return 0

def get_longest_all_palindromes(lst):
    """
    determina cea mai lunga subsecv de palindroame
    """
    l = len(lst)
    result = []
    for i in range(l):
        for j in range(i, l):
            k = is_palindrome(lst[i])
            all_palindromes = True
            for num in lst[i:j + 1]:
                if is_palindrome(num) != k:
                    all_palindromes = False
                    break
            if all_palindromes:
                if j - i + 1 > len(result):
                    result = lst[i:j + 1]
    return result

def read_array(lst, length):
    print("Introduceti numerele sirului: ")
    for i in range(length):
        lst.append(int(input()))

def read_statements():
    problem = input("Introduceti numarul problemei ")
    length = int(input("Introduceti lungimea sirului: "))
    lst = []
    if problem == "1":
        read_array(lst, length)
        print(get_longest_all_palindromes(lst))
    elif problem == "2":
        k = int(input("Elementul K: "))
        read_array(lst, length)
        get_longest_div_k(lst, k)

def main():
    print("1. Sa se determine cea mai lunga subsecventa de palindroame")
    print("2. Sa se determine cea mai lunga subseceventa divizibila cu k")
    read_statements()

if __name__ == '__main__':
    main()