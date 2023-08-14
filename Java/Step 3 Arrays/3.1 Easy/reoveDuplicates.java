class Solution {
    int remove_duplicate(int A[],int N){
        // code here
       
      //handling edge cases
        if(A.length==0)
            return 0;
        if(A.length==1)
            return 1;
        int j=1; // 1 because we are checking from 1
        for(int i=1;i<A.length;i++){
            if(A[i-1]!=A[i])
                A[j++]=A[i];
        }
        return j;
                
    }
}
