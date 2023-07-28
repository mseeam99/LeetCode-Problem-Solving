/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    nums1.sort((a, b) => a - b); // Sort nums1 in ascending order
    nums2.sort((a, b) => a - b); // Sort nums2 in ascending order
    
    let i = 0;
    let j = 0;
    
    const answer = [];
    
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] === nums2[j]) {
            answer.push(nums1[i]);
            i++;
            j++;
        } else if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
        }
    }
    
    return answer;
};
