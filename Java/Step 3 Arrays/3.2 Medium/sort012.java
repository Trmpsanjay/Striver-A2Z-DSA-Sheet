class Solution {
    public void sortColors(int[] nums) {
       int nextZero = 0;
       int nextTwo = nums.length-1;
       int i = 0;
       while(i<=nextTwo){
           // if nums[i] == 0 swap with next zero and increase nextzero location by 1
           if(nums[i]==0){
               int temp = nums[i];
               nums[i] = nums[nextZero];
               nums[nextZero] = temp;
               nextZero++;
               i++;
           }
           // if nums[i] == 2 swap with next two increase nextTwo location by 1
           else if(nums[i]==2){
               int temp = nums[nextTwo];
               nums[nextTwo] = nums[i];
               nums[i] = temp;
               nextTwo--;
           }else{
               i++;
           }

           //  otherwise increase i
       }
        
    }
}