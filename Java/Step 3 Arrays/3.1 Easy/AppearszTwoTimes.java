
class Sol
{
    public static int search(int A[], int N)
    {
          int xor = A[0];
        for(int i=1;i<A.length;i++){
            xor = A[i]^xor;
        }
        return xor;
    }
}
