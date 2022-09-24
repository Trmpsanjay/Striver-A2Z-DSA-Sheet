public class HighestFrequency {

	public static int highestFrequency(int arr[]) {
		int map[] = new int[99999999];
		for(int i=0;i<arr.length;i++) {
			map[arr[i]]++;
		}
		int max = Integer.MIN_VALUE;
		for(int i=0;i<map.length;i++) {
			max = Math.max(max,map[i]);
		}
		return max;
	}
	public static void main(String[] args) {
		int arr[] = {3,2,2,5,4,4,4,4,4,6,4,4,4,4,4,2,1};
		highestFrequency(arr);
//		 for(int i=0;i<arr.length;i++){
//           System.out.println(arr[i]);
//        }
		System.out.println(highestFrequency(arr));

	}

}
