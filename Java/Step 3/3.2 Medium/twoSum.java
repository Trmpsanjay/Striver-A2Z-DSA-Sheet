class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++ ){
            if(map.containsKey(target-nums[i])){
                int ans[] = {map.get(target-nums[i]),i};
                return ans;
            }
            else{
                map.put(nums[i],i);
            }
        }
        return  new int[2];
    }
}