//arr1,arr2 : the arrays
// n, m: size of arrays
class Solution
{
    //Function to return a list containing the union of the two arrays.
    public static ArrayList<Integer> findUnion(int arr1[], int arr2[], int n, int m)
    {
        HashMap<Integer,Integer> map = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();
        for(int num : arr1){
            if(!map.containsKey(num)){
                map.put(num,1);
                ans.add(num);
            }
        }
        for(int num : arr2){
            if(!map.containsKey(num)){
                map.put(num,1);
                ans.add(num);
            }
        }
        Collections.sort(ans);
        return ans;
    }
}

