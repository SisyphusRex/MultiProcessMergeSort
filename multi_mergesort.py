"""multi merge sort module"""

# System Imports

# First Party Imports
from abstract_mergesort import AbstractMergeSort

# Third Party Imports


class MultiMergeSort(AbstractMergeSort):
    """Multiprocess merge sort class"""

    def sort(self, mergeable: list[int]) -> None:
        """method to sort data"""
