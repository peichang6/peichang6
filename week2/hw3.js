function maxProduct(nums) {
  let length = nums.length;
  let answer = 0
  if (length === 2) {
    answer = nums[0] * nums[1]
    console.log(answer)
    return answer
  } else {
    for (i = 0; i < length; i++) {
      for (j = i + 1; j < length; j++) {

        let product = nums[i] * nums[j];
        if (product > answer) {
          answer = product;
        }
      }
    }
    console.log(answer)
  } return answer
}

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])


