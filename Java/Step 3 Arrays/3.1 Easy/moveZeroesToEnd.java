lass Solution {
    void pushZerosToEnd(int[] arr, int n) {
        // code here
        if(arr.length<=1)
            return;
            int i = 0;
            int j = 0;
            while(j<arr.length){
                if(arr[j]!=0){
                    arr[i] = arr[j];
                    i++;
                }
                j++;
            }
            while(i<arr.length){
                arr[i] = 0;
                i++;
            }
    }
}
