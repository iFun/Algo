public class MaxHeap{
	private int[] heapList;
	private int lastIndex;
	private int size;

	MaxHeap(int size){
		heapList = new int[size];
		lastIndex = 0;
		this.size = size;
	}

	public void createHeap(int[] input){
		for(int i=0;i<input.length;i++){
			insert(input[i]);
		}
	}

	public int getMax(){
		return heapList[0];
	}

	public void insert(int value){
		if(size == lastIndex){
			System.out.println("increase size plz");
		}
		heapList[lastIndex] = value;
		lastIndex++;

		int child = lastIndex - 1;
		int parent = child / 2;
		while(heapList[child] > heapList[parent] && parent >= 0){
			swap(child,parent);
			child = parent;
			parent = child / 2;
		}
	}

	public void print(){
		for (int i = 0; i < lastIndex ; i++) {
			System.out.print(heapList[i] + " ");
		}
		System.out.println("  ");
	}

	private void swap(int i, int j){
		int tmp = heapList[i];
		heapList[i] = heapList[j];
		heapList[j] = tmp;
	}

	public void removeMax(){
		int max = getMax();
		swap(lastIndex - 1,0);
		lastIndex--;

		int parent = 0;
		while((2 * parent) < lastIndex){
			int maxChildren = heapList[2* parent] > heapList[2*parent+1]? 2*parent:2*parent+1;
			if(heapList[maxChildren] > heapList[parent]){
				swap(maxChildren,parent);
				parent = maxChildren;
			}else{
				break;
			}
		}

	}

	public static void main(String[] args) {
		MaxHeap mh = new MaxHeap(10);
		int[] myIntArray = {1000,4,5,100,9,2,101};
		mh.createHeap(myIntArray);
		mh.print();
		mh.removeMax();
		mh.print();

	}

}
