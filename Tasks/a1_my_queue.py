"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.my_queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.my_queue.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.my_queue:
            return None

        else:
            return self.my_queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not self.my_queue:
            return None

        if ind >= len(self.my_queue):
            print("Should return None if no elements there.")

        else:
            return self.my_queue[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.my_queue.clear()

