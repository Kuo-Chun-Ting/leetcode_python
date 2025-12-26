class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        idx_val_arr = [(i, v) for i, v in enumerate(arr)]
        sorted_idx_val_arr = sorted(idx_val_arr, key=lambda x: x[1])
        rev_sorted_idx_val_arr = sorted(idx_val_arr, key=lambda x: x[1], reverse=True)
        oddnext = self.create_next_index(sorted_idx_val_arr)
        evennext = self.create_next_index(rev_sorted_idx_val_arr)

        count = 0
        for i in range(len(arr)):
            curr_idx = i
            step = 1

            while curr_idx < len(arr):
                if curr_idx == len(arr) - 1:
                    count += 1
                    break

                if step % 2 == 1:  # odd steps
                    curr_idx = oddnext[curr_idx]
                else:  # even steps
                    curr_idx = evennext[curr_idx]

                if curr_idx is None:
                    break

                step += 1

        return count

    def create_next_index(self, sorted_idx_val_arr: list[tuple[int, int]]) -> list[int]:
        if not sorted_idx_val_arr:
            return []

        next_index = [None] * len(sorted_idx_val_arr)
        stack: list[int] = []

        for j, v in sorted_idx_val_arr:
            while stack and stack[-1] < j:
                next_index[stack.pop()] = j
            stack.append(j)

        return next_index
