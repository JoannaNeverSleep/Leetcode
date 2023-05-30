class solution:
    def medianOfTwoArray(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2) 
        lens = m + n
        right = -inf
        l1, l2 = 0, 0
        for i in range(lens//2 + 1) :
            left = right 
            if l1 < m and (l2 >= n or nums1[l1] < nums2[l2]):
                right = nums1[l1]
                l1 += 1
            else :
                right = nums2[l2]
                l2 += 1
            
        if lens % 2 ==0:
            return (left + right) / 2.0
        else:
            return right
