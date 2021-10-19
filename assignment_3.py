def get_longest_div_k(lst, k):
        max_div_k = div_k = start = end = 0
        for i in range(len(lst)):
            if lst[i] % k == 0:
                div_k+=1
                if max_div_k < div_k:
                    print(i)
                    max_div_k = div_k
                    start = i - div_k + 1
                    end = i
            else:
                div_k = 0
        
        while start <= end:
            print(lst[start])
            start += 1

def read_array():
    problem = input("Choose the problem: ")
    length = int(input("Read the length of array:"))
    lst = []
    print("Read the array elements:")
    for i in range(length):
        lst.append(int(input()))
    #print(lst)
    if problem == "6":
       k = int(input("K element: "))
       get_longest_div_k(lst, k)



def main():
    read_array()
if __name__ == '__main__':
    main()