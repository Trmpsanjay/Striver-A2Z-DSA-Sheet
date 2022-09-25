class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int curr = 0;
        for(int num : nums){
            if(num==1){
                curr++;
                max = Math.max(curr,max);
            }else{
                curr=0;
            }
        }
        return max;
        
    }
}
