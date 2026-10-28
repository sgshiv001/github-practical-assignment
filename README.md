# Collaborative Development Practical

This repository practises collaborative Git and GitHub workflows through a binary heap lab. Heap Sort orders integers in ascending order, and a priority queue removes the item with the smallest priority number first.

## Run the program

Use Python 3.10 or later:

```text
python src/heap_priority_queue.py
```

Enter integers separated by spaces for Heap Sort. Then enter each priority-queue item as `item priority`; submit a blank line when finished. A smaller priority number means higher priority.

## Run the tests

```text
python -m unittest discover -s tests -v
```

## Project files

- `src/heap_priority_queue.py` implements Heap Sort and a stable min-priority queue.
- `tests/test_heap_priority_queue.py` covers ordering, duplicate values, priority ties, and empty-queue behavior.
- `CONTRIBUTING.md` outlines the fetch, pull, push, pull request, and review workflow.
