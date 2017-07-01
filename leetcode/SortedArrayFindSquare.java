import java.lang.*;

// 给一个sorted integer array， 返回其中每个数的平方组成的array，同样要排序好， 要求O(n)。. 
// 例子：[-3,-1,2,4] 返回 [1,4,9,16]

public class SortedArrayFindSquare{
	public int[] sol(int[] input){
		if(input == null || input.length == 0){
			return input;
		}

		int[] result = new int[input.length];
		int head = 0;
		int tail = input.length - 1;
		int cur = input.length - 1;

		while(cur >= 0){
			if(Math.abs(input[head]) > Math.abs(input[tail])){
				result[cur] = input[head] * input[head];
				head++;
			}else{
				result[cur] = input[tail] * input[tail];
				tail--;
			}
			cur--;
		}
		return result;
	}
	public static void main(String[] args) {
	    int[] input = {-9,-3,-1,2,4};
	    SortedArrayFindSquare s = new SortedArrayFindSquare();

	    int[] result = s.sol(input);

	    for (int i = 0; i < result.length; i++) {
	        System.out.println(result[i]);
	    }
	}
}


