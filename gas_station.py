# time: O(n)
# space: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # finds impossble case, alltogether
        if sum(gas) - sum(cost) < 0:
            return -1

        # finds location of possible case
		# one is quaranteed by spec
		# trick: keep trying from every start pos
		# if the end can be reached (= fuel doesn't run out)
		# it is the correct start pos
        gas_level = 0
        start_at = 0

        for i in range(len(gas)):
            gas_level += gas[i] - cost[i]

            if gas_level < 0:  # gas ran out
                start_at = i + 1  # change the starting point
                gas_level = 0 # reset gas level

        return start_at
