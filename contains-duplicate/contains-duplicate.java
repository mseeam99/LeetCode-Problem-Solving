class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean answer = false;
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]){
                answer=true;
            }
        }
        return answer;
    }   
}