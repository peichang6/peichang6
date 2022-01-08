function twoSum(nums, target) {
  let result = [];
  for (i = 0; i < nums.length; i++) {
    for (j = i + 1; j < nums.length; j++) {
      let sum = nums[i] + nums[j]
      if (sum === target) {
        result.push(i, j)
      }
    }
  } return result
}

let result = twoSum([2, 11, 7, 15], 13);
console.log(result);

