/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

 func guessNumber(n int) int {
    start, end := 1, n
    
    for guess((start + end) / 2) != 0 {
        if guess((start + end) / 2) == -1 {
            end = (start+end) / 2 -1
        } else {
            start = (start+end) / 2 + 1
        }
    }
    
    return (start + end) / 2
}

// Note: (start + end) / 2 could be overflow for bigger constraints, so (start + (end-start)/2) would be safer.