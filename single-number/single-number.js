/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    nums.sort();    
    var last_one = nums.length-1;
    
    if(nums[0]!=nums[1]){
        return nums[0];
    }else if(nums[last_one]!=nums[last_one-1]){
        return nums[last_one];
       }

    for(var i = 1 ; i<=last_one-1; i++){
        if((nums[i]!=nums[i-1]) && (nums[i]!=nums[i+1])){
            return nums[i];
        }
    }
    
};
