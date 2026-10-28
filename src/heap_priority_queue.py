"""Heap Sort and a stable min-priority queue for the lab practical."""

from __future__ import annotations

import heapq
from collections.abc import Iterable


def _sift_down(values: list[int], root: int, stop: int) -> None:
    while True:
        child = 2 * root + 1
        if child >= stop:
            return
        if child + 1 < stop and values[child + 1] > values[child]:
            child += 1
        if values[root] >= values[child]:
            return
        values[root], values[child] = values[child], values[root]
        root = child


def heap_sort(values: Iterable[int]) -> list[int]:
    """Return the input values in ascending order using an in-place max heap."""
    result = list(values)
    length = len(result)

    for root in range(length // 2 - 1, -1, -1):
        _sift_down(result, root, length)

    for end in range(length - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        _sift_down(result, 0, end)

    return result


class PriorityQueue:
    """A stable priority queue where smaller numbers indicate higher priority."""

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, str]] = []
        self._sequence = 0

    def enqueue(self, item: str, priority: int) -> None:
        heapq.heappush(self._heap, (priority, self._sequence, item))
        self._sequence += 1

    def peek(self) -> tuple[str, int]:
        if not self._heap:
            raise IndexError("peek from an empty priority queue")
        priority, _, item = self._heap[0]
        return item, priority

    def dequeue(self) -> tuple[str, int]:
        if not self._heap:
            raise IndexError("dequeue from an empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return item, priority

    def in_priority_order(self) -> list[tuple[str, int]]:
        return [
            (item, priority)
            for priority, _, item in sorted(self._heap)
        ]

    def __len__(self) -> int:
        return len(self._heap)


def _read_priority_queue() -> PriorityQueue:
    queue = PriorityQueue()
    print("Enter each item followed by its priority. Press Enter on a blank line to finish.")
    while entry := input("> ").strip():
        try:
            item, priority_text = entry.rsplit(maxsplit=1)
            queue.enqueue(item, int(priority_text))
        except ValueError:
            print("Use the format: item priority (for example, report 2).")
    return queue


def main() -> None:
    raw_numbers = input("Enter integers separated by spaces: ").strip()
    try:
        numbers = [int(value) for value in raw_numbers.split()]
    except ValueError:
        print("Please enter integers separated by spaces.")
        return

    print(f"Sorted array: {heap_sort(numbers)}")
    print(f"Number of elements sorted: {len(numbers)}")

    queue = _read_priority_queue()
    if not queue:
        print("The priority queue is empty.")
        return

    item, priority = queue.peek()
    print(f"Highest-priority element: {item} (priority {priority})")
    removed_item, removed_priority = queue.dequeue()
    print(f"Removed element: {removed_item} (priority {removed_priority})")
    print(f"Remaining elements: {queue.in_priority_order()}")


if __name__ == "__main__":
    main()
