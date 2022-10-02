class Solution {
    public pair[] allPairs( long A[], long B[], long N, long M, long X) {
        // Your code goes here 
          // Your code goes here
        Arrays.sort(A);
        Arrays.sort(B);
        HashMap<Long,Long> hm = new HashMap<>();
         ArrayList<pair> p = new ArrayList<>();
        for(int i=0;i<M;i++)
        hm.put(B[i],hm.getOrDefault(B[i],0L)+1);
        
        for(int i=0;i<N;i++)
        {
            if(hm.containsKey(X-A[i]))
            {
                p.add(new pair(A[i],X-A[i]));
                hm.put(X-A[i],hm.get(X-A[i])-1);
            }
        }
        return p.toArray(new pair[p.size()]);
    }
}
