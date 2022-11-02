class Solution:
    
    def get_sum_of_numbers_in_list(self, lst):
        sum = 0
        for i in lst:
            sum = sum + i  
        return sum 
    
    def runningSum(self, nums: List[int]) -> List[int]:
        # result = list()
        # result[0] = nums[0]
        previous_elements = list()
        for index,number in enumerate(nums):
            
            previous_elements.append(number)
            nums[index] = self.get_sum_of_numbers_in_list(previous_elements)
        return nums
            
            
    
    
    