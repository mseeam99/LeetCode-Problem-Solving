class Solution {
    public int findMin(int[] nums) {
        if (nums[0] < nums[nums.length - 1]) {
            return nums[0];
        }

        return findRotated(nums, 0, nums.length - 1);
    }

    private int findRotated(int[] nums, int start, int end) {
        int n = nums.length;
        
        // two elements left
        if (end - start == 1) {
            return Math.min(nums[end], nums[start]);
        }

        if (end > start) {
            int mid = (start + end) / 2;
            
            if (nums[mid] <= nums[start] && nums[mid] < nums[end])
                return findRotated(nums, start, mid);
            else 
                return Math.min(
                    findRotated(nums, mid + 1, end),
                    findRotated(nums, start, mid));
        }
        
        return nums[end];
    }
}