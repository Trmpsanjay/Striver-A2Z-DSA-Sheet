class Solution {
    private static void reverse(int nums[],int i, int j){
        while(i<j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        if(nums.length==0 || nums.length==1)
            return;
        int i =0;
        int j = k;
        // rotating first k elements
        reverse(nums,0,nums.length-k-1);
         // rotating n-k elements
        reverse(nums,nums.length-k,nums.length-1);
         // now rotating whole array
        reverse(nums,0,nums.length-1);
    }
}
