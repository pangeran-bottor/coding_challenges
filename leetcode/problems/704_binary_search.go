func search(nums []int, target int) int {
	return binarySearch(0, len(nums) - 1, nums, target)
}

func binarySearch(start int, end int, nums []int, target int) int {
	if start > end {
		return -1
	}

	mid := (start + end) / 2
	if nums[mid] == target {
		return mid
	} else if nums[mid] < target {
		return binarySearch(mid + 1, end, nums, target)
	}

	return binarySearch(start, mid - 1, nums, target)
}
