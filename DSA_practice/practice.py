''' 
     Finding a pair of numbers that add up to a target sum in a sorted or unsorted array.
'''
import time

# not good approach 
'''def find_pair_of_number_brute_force(arr,x): # brute force approach  O(n*n) quadratic complexity   
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            print(arr[i],arr[j])
            time.sleep(0.5)
            if arr[i] + arr[j] == x:
                return arr[i],arr[j]'''
            


# def find_pair_of_num_using_two_pointer(arr,x): # O(n) liner complexity
#     f = 0
#     b = len(arr)-1
#     while f < b:
#         print(arr[f],arr[b])
#         time.sleep(0.5)
#         sum_ = arr[f] + arr[b]
#         if sum_ == x:
#             return arr[f],arr[b]
#         elif sum_ < x:
#             f += 1
#         else:  # sum_ > x
#             b -= 1


# arr = [2, 3, 5, 8, 11]

def find_pair_sorted_list(arr,t):
    s_arr = sorted(arr)
    f = 0
    b = len(s_arr)-1
    while f < b:
        print(s_arr[f],s_arr[b])
        time.sleep(0.5)
        sum_ = s_arr[f] + s_arr[b]
        if sum_ == t:
            return s_arr[f], s_arr[b]
        elif sum_ < t:
            f += 1
        else:

            b = b-1
    return None



        

if __name__=='__main__':
    #arr = [2,4,8,12,15,20,21,22,45,67,87,98,111,121,122,123,124,125,126,345,400]
    arr = [3,5,2,8,11]
    x = 16

    #print(find_pair_of_number_brute_force(arr,x))
    #print(find_pair_of_num_using_two_pointer(arr,x))
    print(find_pair_sorted_list(arr,x))






