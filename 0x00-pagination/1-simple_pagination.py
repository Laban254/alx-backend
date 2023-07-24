#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dataset for a given datarange"""

        try:
            assert page > 0 or page_size > 0
            assert type(page) is int or type(page_size) is int
            pages = index_range(page, page_size)
            dataset = self.dataset()[pages[0]:pages[1]]
            return dataset
        except Exception:
            return []


def index_range(page, page_size) -> tuple:
    """named index_range that takes two integer
    arguments page and page_size
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
