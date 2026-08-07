class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        main = []
        temp = []
        ptr1= 0
        ptr2 = 1
        i=1
        while ptr1<len(nums):
            temp = []
            temp.append(nums[ptr1])
            while ptr2<len(nums):
                if nums[ptr2]==i+nums[ptr1]:
                    temp.append(nums[ptr2])
                    print(temp)
                else:
                    if len(temp)==1:
                        main.append(str(temp[0]))
                        print(main)
                    else:
                        main.append(str(temp[0]) + "->" + str(temp[len(temp)-1]))
                        print(main)
                    break
                ptr2 +=1
                i+=1
            ptr1 = ptr2
            ptr2+=1
            i=1
        if len(temp)==1:
            main.append(str(temp[0]))
            print(main)
        elif len(temp)>1:
            main.append(str(temp[0]) + "->" + str(temp[len(temp)-1]))
            print(main)
        return main
                
                


