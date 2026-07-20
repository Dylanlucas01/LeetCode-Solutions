class DataEntry:
    def __init__(self, minute: int, value: str):
        self.minute = minute
        self.value = value


class TimeMap:
    def __init__(self):
        self.data_set: dict[str, list[DataEntry]] = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        minute = timestamp

        if key not in self.data_set:
            self.data_set[key] = []

        data_entry = DataEntry(minute,value)
        self.data_set[key].append(data_entry)
        
    def get(self, key: str, timestamp: int) -> str:
        target_minute = timestamp

        if key not in self.data_set:
            return ""

        data_entry_list = self.data_set[key]

        left = 0
        right = len(data_entry_list)-1
        data_entry_value = ""

        while left <= right:
            middle = (left+right)//2
            middle_data_entry = data_entry_list[middle]

            if middle_data_entry.minute <= target_minute:
                data_entry_value = middle_data_entry.value
                left = middle + 1
            
            else:
                right = middle -1
        return data_entry_value

        """
        {
            "username":
            [
                (1, "alice"),
                (5, "alice99"),
                (10, "alice_dev")
            ],

            "guest":
            [
                (1, "guest_user"),
                (5, "guest_user00"),
                (10, "guest_user_dev")
            ]
        }
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)