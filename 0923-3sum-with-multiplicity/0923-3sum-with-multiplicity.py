from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        modu = pow(10, 9)+7
        i = 0
        count = 0 
        arr.sort()
        n = len(arr)
        while i<n:
            j = i+1
            k = n-1
            while j<k and i<j:
                sum3 = arr[i]+arr[j]+arr[k]
                if sum3==target:
                    if arr[i]==arr[j]==arr[k]:
                        temp = counter[arr[i]]
                        count+=(temp*(temp-1)*(temp-2))//6
                        break
                    elif arr[i]!=arr[j] and arr[j]!=arr[k] and arr[i]!=arr[k]:
                        count+=(counter[arr[i]]*counter[arr[j]]*counter[arr[k]])
                    else:
                        if arr[i]==arr[j]:
                            temp = counter[arr[i]]
                            temp2 = counter[arr[k]]
                        elif arr[j]==arr[k]:
                            temp = counter[arr[j]]
                            temp2 = counter[arr[i]]
                        else:
                            temp =counter[arr[i]]
                            temp2 = counter[arr[j]]
                        # print(temp, temp2, arr[i], arr[j], arr[k], count, i, j, k)
                        count+=(temp*(temp-1)//2*temp2)
                    while k>j and arr[k]==arr[k-1]:
                        k-=1
                    k-=1
                    while k>j and arr[j]==arr[j+1]:
                        j+=1
                    j+=1
                elif sum3>target:
                    while k>j and arr[k]==arr[k-1]:
                        k-=1
                    k-=1
                else:
                    while k>j and arr[j]==arr[j+1]:
                        j+=1
                    j+=1
            while i<n-1 and arr[i]==arr[i+1]:
                i+=1
            i+=1
            count = count%modu
        return count
                                            
                    
                        
                