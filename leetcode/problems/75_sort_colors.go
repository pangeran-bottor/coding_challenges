func sortColors(nums []int) {
	counts := make(map[int]int)
	for _, num := range nums {
		counts[num] += 1
	}

	pointer := 0
	for _, color := range []int{0, 1, 2} {
		for i := 0; i < counts[color]; i++ {
			nums[pointer] = color
			pointer++
		}
	}
}