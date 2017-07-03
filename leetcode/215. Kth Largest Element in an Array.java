public class Solution {
  public int findKthLargest(int[] nums, int k) {
    return quickSelect(nums, 0, nums.length - 1, k);
  }



  //[1,-1,2,10,3]
  // choose pivot as last elemnt
  //left = 0 ; right = pivot -1
  // if left is out of position swap with right and decrease right since the right element now is inposition
  private int quickSelect(int[] nums, int start, int end, int k) {
    int pivot = end;
    int left = start;
    int right = end - 1;
    while (left <= right) {
      if (nums[left] > nums[pivot]) {
        swap(nums, left, right);
        right--;
      } else {
        left++;
      }
    }
    swap(nums, left, pivot);

    int rank = nums.length - left;
    if (rank == k) return nums[left];
    if (rank > k) return quickSelect(nums, left + 1, end, k);
    return quickSelect(nums, start, left - 1, k);
  }

  private void swap(int[] nums, int a, int b) {
    int tmp = nums[a];
    nums[a] = nums[b];
    nums[b] = tmp;
  }
}
