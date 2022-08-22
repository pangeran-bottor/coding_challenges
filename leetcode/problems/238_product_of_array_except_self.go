func productExceptSelf(nums []int) []int {
	N := len(nums)
	ret := make([]int, N)
	for idx, _ := range nums {
		ret[idx] = 1
	}

	multiplier := 1
	for i := 1; i < N; i++ {
		multiplier *= nums[i-1]
		ret[i] *= multiplier
	}

	multiplier = 1
	for i := N - 2; i > -1; i-- {
		multiplier *= nums[i+1]
		ret[i] *= multiplier
	}
	return ret
}
