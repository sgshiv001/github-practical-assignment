import unittest

from src.heap_priority_queue import PriorityQueue, heap_sort


class HeapSortTests(unittest.TestCase):
    def test_sorts_values_ascending(self) -> None:
        self.assertEqual(heap_sort([7, 2, 9, 1, 2]), [1, 2, 2, 7, 9])

    def test_handles_empty_and_single_value_inputs(self) -> None:
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([4]), [4])


class PriorityQueueTests(unittest.TestCase):
    def test_removes_smallest_priority_first(self) -> None:
        queue = PriorityQueue()
        queue.enqueue("normal", 3)
        queue.enqueue("urgent", 1)

        self.assertEqual(queue.peek(), ("urgent", 1))
        self.assertEqual(queue.dequeue(), ("urgent", 1))
        self.assertEqual(queue.in_priority_order(), [("normal", 3)])

    def test_keeps_equal_priorities_in_insertion_order(self) -> None:
        queue = PriorityQueue()
        queue.enqueue("first", 2)
        queue.enqueue("second", 2)

        self.assertEqual(queue.dequeue(), ("first", 2))
        self.assertEqual(queue.dequeue(), ("second", 2))

    def test_empty_queue_operations_raise_index_error(self) -> None:
        queue = PriorityQueue()
        with self.assertRaises(IndexError):
            queue.peek()
        with self.assertRaises(IndexError):
            queue.dequeue()


if __name__ == "__main__":
    unittest.main()
