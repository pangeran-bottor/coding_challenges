func numJewelsInStones(jewels string, stones string) int {
	result := 0
	jewelsMap := make(map[string]bool)

	for _, j := range jewels {
		jCh := fmt.Sprintf("%c", j)
		jewelsMap[jCh] = true
	}

	for _, s := range stones {
		sCh := fmt.Sprintf("%c", s)
		if jewelsMap[sCh] {
			result += 1
		}
	}
	return result
}