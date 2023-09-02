import time


def get_pair_from_unsorted_arr(arr,t): # brute force approach time complexity O(n**2)
    l = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
           # time.sleep(0.5)
            print(arr[i],arr[j])
            if arr[i] + arr[j] == t:
                l.append((arr[i],arr[j]))
                #return arr[i],arr[j]
    return l

'''def find_all_pair_unsorted_arr(arr,t):
    s_arr = sorted(arr)
    l = []
    f = 0
    b = len(s_arr)-1
    while f < b:
        print(s_arr[f],s_arr[b])
        time.sleep(0.5)
        sum_ = s_arr[f] + s_arr[b]
        if sum_ == t:
            l.append((s_arr[f],s_arr[b]))
            #return s_arr[f], s_arr[b]

        elif sum_ < t:
            f += 1
        else:

            b = b-1
    return s_arr
'''



def find_all_pair_unsorted_arr(arr, t):
    s_arr = sorted(arr)
    l = []
    f = 0
    b = len(s_arr) - 1
    while f < b:
        print(s_arr[f],s_arr[b])
        time.sleep(0.5)
        sum_ = s_arr[f] + s_arr[b]
        if sum_ == t:
            l.append((s_arr[f], s_arr[b]))
            print('yess this match added to list')
            f += 1
            b -= 1
        elif sum_ < t:
            f += 1
        else:
            b = b - 1
    return l



if __name__=='__main__':
    #arr = [0,3,5,1,2,9,6,15,10]
    arr = [5,3,9,15,4,6,1,0,9]
    s = sorted(arr)
    print(s)
    t = 18

    #result = get_pair_from_unsorted_arr(arr,t)
    result =  find_all_pair_unsorted_arr(arr,t)
    print(result)