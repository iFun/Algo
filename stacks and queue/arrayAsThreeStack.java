//implement 3 stacks using one array
class FixedMultiStack {
	private int numberOfStacks = 3;
	private int stackCapacity;
	private int[] values;
	private int[] size;

	public FixedMultiStack(int stackSize){
		stackCapacity = stackSize;
		values = new int[stackSize * numberOfStacks];
		size = new int[numberOfStacks];
	}

	public boolean push(int stackNum, int value){
		if(isFull(stackNum)){
			System.out.println("stack is full");
			return false;
		}else{
			int offset = stackCapacity * (stackNum - 1) + size[stackNum - 1];
			values[offset] = value;
			size[stackNum - 1] += 1;
			return true;
		}
	}

	public int pop(int stackNum){
		if(isEmpty(stackNum)){
			System.out.println("stack is empty");
			return -1;
		}else{
			int offset = stackCapacity * (stackNum - 1) + size[stackNum - 1];
			int result = values[offset - 1];
			values[offset - 1] = 0;
			size[stackNum - 1] -= 1;
			return result;
		}
	}

	public boolean isFull(int stackNum){
		return size[stackNum - 1] == stackCapacity;
	}

	public boolean isEmpty(int stackNum){
		return size[stackNum - 1] == 0;
	}
	public void print(int stackNum){
		if(isEmpty(stackNum)){
			System.out.println("stack is empty");
		}else{
			int offset = stackCapacity * (stackNum - 1);
			for(int i = offset; i < offset + size[stackNum - 1]; i++){
				System.out.println(values[i]);
			}
		}
	}
}


public class arrayAsThreeStack {
   public static void main(String[] args) {
      FixedMultiStack fms = new FixedMultiStack(5);
      fms.push(1,1);
      fms.push(1,2);
      fms.push(1,3);
      fms.push(2,33);
      fms.push(2,34);
      fms.push(2,35);
      fms.pop(1);
      fms.push(1,300);
      fms.push(1,300);
      fms.push(1,300);
      fms.push(3,222);
      fms.pop(1);
      fms.pop(2);
      fms.print(1);
      fms.print(2);
      fms.print(3);
   }
}