def largestPalindromic(self, num: str) -> str:
	c = Counter(num)
	s = mid = ""

	for k in sorted(c.keys(), reverse=True):
		mid = max(mid, k * (c[k] & 1))
		s += k * (c[k] // 2)

	s = s.lstrip('0')
	return (s + mid + s[::-1]) or "0"
