
class Solution {
    public int[] rearrangeArray(int[] nums) {
        // brute force

        // #segrating positive and negative
       int[] positive = new int[nums.length/2];
       int[] negative = new int[nums.length/2];
       int posIndex = 0;
       int negIndex = 0;
       for(int num : nums){
           if (num > 0 ){
               positive[posIndex++] = num;
           }else{
               negative[negIndex++] = num;
           }
       }

    //    # now copying positive + negative
       int ans[] = new int[nums.length];
       int j = 0;
       for(int i=0;i<nums.length/2;i++){
           ans[j++] = positive[i];
           ans[j++] = negative[i];
       }
       return ans;
    }
}
// optimal

//  int posIndex = 0;
//     int negIndex = 1;
//     int ans [] = new int[nums.length];
//     for(int num : nums){
//         if(num > 0){
//             ans[posIndex] = num;
//             posIndex+=2;
//         }else{
//             ans[negIndex] = num;
//             negIndex+=2;
//         }
//     }
//     return ans;
