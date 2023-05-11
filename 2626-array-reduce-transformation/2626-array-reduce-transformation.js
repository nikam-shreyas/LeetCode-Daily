/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let t = init;
    for(let i=0;i<nums.length;i++){
        t = fn(t, nums[i]);
    }
    return t;
};