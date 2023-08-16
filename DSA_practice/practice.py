''' 
     Finding a pair of numbers that add up to a target sum in a sorted or unsorted array.
'''
import time

# not good approach 
def find_pair_of_number_brute_force(arr,x): # brute force approach  O(n*n) quadratic complexity   
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            print(arr[i],arr[j])
            time.sleep(0.5)
            if arr[i] + arr[j] == x:
                return arr[i],arr[j]
            


        

if __name__=='__main__':
    arr = [2,4,8,12,15,20,21,22,45,67,87,98,111,121,122,123,124,125,126,345,400]
    x = 745

    #print(find_pair_of_number_brute_force(arr,x))
    print(find_pair_of_num_using_two_pointer(arr,x))






