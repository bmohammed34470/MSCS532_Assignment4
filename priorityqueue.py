class Task:
    """
    Represents a task with a unique ID, priority, arrival time, and deadline.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority}, Arrival={self.arrival_time}, Deadline={self.deadline})"


class PriorityQueue:
    """
    A priority queue implementation using a max-heap.
    """
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Inserts a task into the priority queue.
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Removes and returns the task with the highest priority.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task, new_priority):
        """
        Increases the priority of a specific task and adjusts its position in the heap.
        """
        for i, t in enumerate(self.heap):
            if t.task_id == task.task_id:
                t.priority = new_priority
                self._heapify_up(i)
                break

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        """
        return len(self.heap) == 0

    def _heapify_up(self, index):
        """
        Restores the heap property by moving a task up the heap.
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent_index].priority:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        """
        Restores the heap property by moving a task down the heap.
        """
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            largest = index

            if left_child < len(self.heap) and self.heap[left_child].priority > self.heap[largest].priority:
                largest = left_child
            if right_child < len(self.heap) and self.heap[right_child].priority > self.heap[largest].priority:
                largest = right_child

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break


def heapsort(tasks):
    """
    Sorts a list of tasks in descending order of priority using Heapsort.
    """
    pq = PriorityQueue()
    for task in tasks:
        pq.insert(task)
    sorted_tasks = []
    while not pq.is_empty():
        sorted_tasks.append(pq.extract_max())
    return sorted_tasks


# Example Usage
if __name__ == "__main__":
    # Create some tasks
    tasks = [
        Task(1, 5, 0, 10),
        Task(2, 3, 1, 8),
        Task(3, 8, 2, 12),
        Task(4, 1, 3, 15)
    ]

    # Insert tasks into the priority queue
    pq = PriorityQueue()
    for task in tasks:
        pq.insert(task)
        print(f"Inserted: {task}")

    # Extract tasks in order of priority
    print("\nExtracting tasks in order of priority:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Extracted: {task}")

    # Test Heapsort
    print("\nSorting tasks using Heapsort:")
    sorted_tasks = heapsort(tasks)
    for task in sorted_tasks:
        print(task)