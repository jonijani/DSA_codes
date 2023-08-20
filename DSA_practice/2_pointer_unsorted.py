import time


def get_pair_from_unsorted_arr(arr,t): # brute force approach time complexity O(n**2)
    l = []
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
           # time.sleep(0.5)
            print(arr[i],arr[j])
            if arr[i] + arr[j] == t:
                l.append((arr[i],arr[j]))
                #return arr[i],arr[j]
    return l







if _name=='main_':
    arr = [0,3,5,1,2,9,6,15,10]
    t = 26

    result = get_pair_from_unsorted_arr(arr,t)
    print(result)