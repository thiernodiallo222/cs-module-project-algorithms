'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    if (len(arr) > 1):
        for i in range(0, len(arr)):
            count =1
            for j in range(0,len(arr)):
                if (i != j and arr[i] == arr[j]):
                    count += 1
            if count == 1:
                return arr[i]
    else:
        return arr[0]      
      
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")