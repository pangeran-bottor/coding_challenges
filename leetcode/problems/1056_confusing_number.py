class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalids = "23457"
        n_str = str(n)

        for ch in n_str:
            if ch in invalids:
                return False
        
        rotate_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        rotated_ch = []
        for i in range(len(n_str)-1, -1, -1):
            rotated_ch.append(rotate_map[n_str[i]])
        rotated_int = int("".join(rotated_ch))

        return n != rotated_int
