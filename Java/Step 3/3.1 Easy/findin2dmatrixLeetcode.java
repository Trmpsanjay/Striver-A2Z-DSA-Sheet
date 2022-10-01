class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // brute force
        // for(int i=0;i<matrix.length;i++){
        //     for(int j=0;j<matrix[i].length;j++){
        //         if(matrix[i][j]==target)
        //             return true;
        //     }
        // }
        // return false;

        // optimal
        // if(matrix.length==1 && matrix[0].length==1){
        //     if(matrix[0][0]==target) return true;
        //     else return false;
        // }
        int i = 0;
        int j = matrix[0].length-1;
        while(i<matrix.length && j>=0){
            int num = matrix[i][j];
            if(num==target)
                return true;
            else if(num>target){
                j--;
            }else{
                i++;
            }
        }
        return false;
        
    }
}
