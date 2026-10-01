class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        n=n1+n2
        ind2=n//2
        ind1=ind2-1
        cnt=0
        ind1el,ind2el=-1,-1
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                if cnt==ind1:
                    ind1el=nums1[i]
                if cnt==ind2:
                    ind2el=nums1[i]
                cnt+=1
                i+=1
            else:
                if cnt==ind1:
                    ind1el=nums2[j]
                if cnt==ind2:
                    ind2el=nums2[j]
                cnt+=1
                j+=1
        while i<n1:
                if cnt==ind1:
                    ind1el=nums1[i]
                if cnt==ind2:
                    ind2el=nums1[i]
                cnt+=1
                i+=1
        while j<n2:
            if cnt==ind1:
                ind1el=nums2[j]
            if cnt==ind2:
                ind2el=nums2[j]
            cnt+=1
            j+=1
        if n%2==1:
            return float(ind2el)
        return float((ind1el+ind2el)/2)
            
        