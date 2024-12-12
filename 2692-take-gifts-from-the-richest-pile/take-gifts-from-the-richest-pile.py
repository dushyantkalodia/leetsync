class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert to a max-heap by negating the values
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        while k > 0:
            # Pop the largest element (negated back to positive)
            maxEl = -heapq.heappop(gifts)
            # Calculate the remaining gift value after taking the square root
            remaining = int(math.sqrt(maxEl))
            # Push the remaining value back into the heap (negated again)
            heapq.heappush(gifts, -remaining)
            k -= 1

        # Calculate the sum of remaining gifts (negated back to positive)
        return -sum(gifts)