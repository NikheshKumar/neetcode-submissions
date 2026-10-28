class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q = deque(students)
        count = 0
        l = 0

        while q and count < len(q):
            if q[0]==sandwiches[l]:
                q.popleft()
                l += 1
                count = 0
            else:
                q.append(q.popleft())
                count += 1

        return len(q) 



        