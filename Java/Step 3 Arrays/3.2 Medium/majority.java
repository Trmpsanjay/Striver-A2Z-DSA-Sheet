class Solution {
    public int majorityElement(int[] nums) {

        int majorityNum = (int)Math.floor(nums.length/2);
        HashMap<Integer,Integer> map = new HashMap<>();
        for( int num : nums){
            if(map.containsKey(num)){
                int count = map.get(num);
                if(count+1>majorityNum){
                    return num;
                }
                map.put(num,count+1);

            }else{
                map.put(num,1);
            }
        }
        return 1;

        
    }
}