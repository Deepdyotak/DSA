'''I am glad you came, lemme explain the question properly to you.. for example let's say the given array is [1,2,3,4] and the pairs are going to be [1,2] and [3,4].. that's right, you take two elements and another two elements until the end of the array.. and what you are expected to do is.. take the first pair [1,2] and this means there should be ONLY ONE '2' as the first element of the array which you gonna give as the answer, then take the second pair [3,4] and this means, there are going to be THREE '4s' next to each other as the following elements of the array which you gonna give as the answer, so is gonna look like this
[2,4,4,4] -> the first element is ONLY ONE '2' from which we got from the first pair and the following THREE '4s' we go from our second pair.. you are welcome'''



class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out=[]
        # to traverse in pairs
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                 out.append(nums[i+1])

           
        return out
             
           

            



        
