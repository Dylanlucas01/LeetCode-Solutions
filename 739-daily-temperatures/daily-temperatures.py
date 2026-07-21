class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = []
        waiting_days = [0] * len(temperatures)

        for current_index in range(len(temperatures)):
            current_temp = temperatures[current_index]

            while index_stack and current_temp > temperatures[index_stack[-1]]:
                previous_index = index_stack.pop()
                waiting_days[previous_index] = current_index - previous_index

            index_stack.append(current_index)

        return waiting_days