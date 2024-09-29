import time
import stringdata

def linear_search(arr, key):
    # O(n)
    for index, ele in enumerate(arr):
        if ele == key:
            return index
    return -1 

def binary_search(arr, key):
    # O(log(n))
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if key == arr[middle]:
            return middle
        elif key > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def main():
    mydata = stringdata.get_data()
    #ydata.sort()  # Ensure the data is sorted for binary search

    # Linear search
    start = time.time()
    linear_search(mydata, "aaaaa")
    end = time.time()
    diff = end - start
    print(f"The time for linear search for 'aaaaa': {diff}")

    # Binary search
    start = time.time()
    binary_search(mydata, "aaaaa")
    end = time.time()
    diff = end - start
    print(f"The time for binary search for 'aaaaa': {diff}")

if __name__ == "__main__":
    main()
