class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        no_of_white_blocks = 0
        min_blocks_to_recolor = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                no_of_white_blocks += 1  # Count white blocks in the current window

            # When the window reaches size k
            if right - left + 1 == k:
                min_blocks_to_recolor = min(min_blocks_to_recolor, no_of_white_blocks)  # Update minimum recoloring needed

                # If all blocks in the window are already black, return immediately
                if min_blocks_to_recolor == 0:
                    return 0

                # Slide the window: If the leftmost block is white, decrement count
                if blocks[left] == 'W':
                    no_of_white_blocks -= 1
                
                left += 1  # Move the window forward

        return min_blocks_to_recolor