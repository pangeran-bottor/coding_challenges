func isPerfectSquare(num int) bool {
    start, end := 1, num
    
    for start <= end {
        mid := start + (end-start)/2
        if mid * mid == num {
            return true
        } else if mid * mid < num {
            start = mid + 1
        } else {
            end = mid -1
        }
    }
    
    return false
}
