class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        # Step 1: Store the number of security devices in each row
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]

        # Step 2: Initialize total beams
        total_beams = 0

        # Step 3: Multiply adjacent rows’ device counts
        for i in range(1, len(device_counts)):
            total_beams += device_counts[i - 1] * device_counts[i]

        return total_beams
