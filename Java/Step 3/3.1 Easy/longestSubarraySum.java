 // Function for finding maximum and value pair
    public static int lenOfLongSubarr (int A[], int N, int K) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int maxLength = 0;
        int sum = 0;
        // map.put(0,0);
        for(int i=0; i<A.length;i++){
            sum+=A[i];
            if(sum==K){
                maxLength=i+1;
            }
             if(!map.containsKey(sum)){ // do not update because we need minimum index for that sum
                map.put(sum,i);
            }
            if(map.containsKey(sum-K)){
                int diff = i-map.get(sum-K);;
                maxLength = Math.max(maxLength,diff);
            }
           
        }
        return maxLength;
    }
    
