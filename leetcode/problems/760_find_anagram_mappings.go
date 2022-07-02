func anagramMappings(nums1 []int, nums2 []int) []int {
	result := make([]int, len(nums1))
	numsMap := make(map[int]int)
	for idx, num := range nums2 {
		numsMap[num] = idx
	}

	for idx, num := range nums1 {
		result[idx] = numsMap[num]
	}
	return result
}