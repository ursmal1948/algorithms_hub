import pytest
from algorithms.sorting import (
    QuickSort,
    BubbleSort,
    MergeSort,
    SelectionSort,
    SortingManager
)


class TestSortingAlgorithms:

    @pytest.mark.parametrize('items_and_sorted_items', [
        ([10, -5, 29, -300, 200, 12, 45, 90, 33, 120, 17], [-300, -5, 10, 12, 17, 29, 33, 45, 90, 120, 200]),
        (['dog', 'lion', 'cat', 'anaconda', 'tiger'], ['anaconda', 'cat', 'dog', 'lion', 'tiger'])

    ])
    @pytest.mark.parametrize('sorting_algorithm', [
        QuickSort(),
        BubbleSort(),
        MergeSort(),
        SelectionSort()
    ])
    def test_sorting(self, sorting_algorithm, items_and_sorted_items):
        sorting_manager = SortingManager(sorting_algorithm)
        data, expected_result = items_and_sorted_items
        # sorting_algorithm.sort = MagicMock(return_value=expected_result)
        result = sorting_manager.perform_sorting(data)
        assert result == expected_result


class TestSortingManager:
    def test_set_sorting_strategy(self):
        sorting_manager = SortingManager(QuickSort())
        new_strategy = BubbleSort()
        sorting_manager.set_sorting_strategy(new_strategy)
        assert sorting_manager.sorting_strategy == new_strategy

    def test_perform_sorting(self, items_and_expected_sorted_items):
        sorting_manager = SortingManager(QuickSort())
        data, expected_result = items_and_expected_sorted_items
        sorted_data = sorting_manager.perform_sorting(data)
        assert sorted_data == expected_result