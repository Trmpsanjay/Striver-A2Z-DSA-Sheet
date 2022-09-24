class Solution{
    private static int binarySearch(int arr[],int low,int high,int K){
        if(low>high){
            return -1;
        }
        int mid = (low+high)/2;
        if(arr[mid]==K){
             return 1;
        }
        else if(arr[mid]<K){
            return binarySearch(arr,mid+1,high,K);
        }else{
            return binarySearch(arr,low,mid-1,K);
        }
    }
    static int searchInSorted(int arr[], int N, int K)
    {
        return binarySearch(arr,0,N-1,K);
        
        // Your code here
        
    }
}
