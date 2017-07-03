public class QuickSort{
	private int[] numbers;

	public int[] sort(int[] input){
		this.numbers = input;
		quickSort(0,input.length - 1);
		return numbers;

	}

	public void quickSort(int low, int high){
		int small = low;
		int large = high;
		int pivot = numbers[low + (high - low) / 2]; // get the middle

		while(small < large){
			while(numbers[small] < pivot){
				small++;
			} 
			while(numbers[large] > pivot){
				large--;
			}
			if(small <= large){
				exchange(small,large);
				small++;
				large--;
			}
		}

		if(low < large){
			quickSort(low,large);
		}
		if(high > small){
			quickSort(small, high);
		}
	}



	public void exchange(int x, int y){
		int tmp = numbers[x];
		numbers[x] = numbers[y];
		numbers[y] = tmp;
	}


	public static void main(String[] args) {
		int[] input = {44,123,1,-9,-33,-1,2,42,100};

		QuickSort qs = new QuickSort();
		int [] result = qs.sort(input);

		for (int i = 0; i < result.length; i++) {
	        System.out.print(result[i] + " ");
	    }
	    System.out.println("  ");
	}
}
