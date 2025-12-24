class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        
        # Sort capacities in descending order
        capacity.sort(reverse=True)
        
        current_capacity = 0
        box_count = 0
        
        for cap in capacity:
            current_capacity += cap
            box_count += 1
            
            if current_capacity >= total_apples:
                return box_count
