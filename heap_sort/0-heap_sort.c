#include "sort.h"

/**
 * swap - swaps two integers
 * @a: first integer
 * @b: second integer
 */
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

/**
 * sift_down - Maintains the heap property between parent and children
 * @array: Array to sort
 * @size: Total size of the array
 * @start: Index of the root element of the heap
 * @end: Last index of the heap
 */
void sift_down(int *array, size_t size, size_t start, size_t end)
{
    size_t root = start;
    size_t child, swap_idx;

    while ((root * 2) + 1 <= end)
    {
        child = (root * 2) + 1;
        swap_idx = root;

        if (array[swap_idx] < array[child])
            swap_idx = child;
        if (child + 1 <= end && array[swap_idx] < array[child + 1])
            swap_idx = child + 1;
        if (swap_idx == root)
            return;
        else
        {
            swap(&array[root], &array[swap_idx]);
            print_array(array, size);
            root = swap_idx;
        }
    }
}

/**
 * heap_sort - sorts an array of integers in ascending order using Heap sort
 * @array: Array to sort
 * @size: Size of the array
 */
void heap_sort(int *array, size_t size)
{
  int start, end;

    if (!array || size < 2)
        return;

    /* Build the max heap */
    start = (size - 2) / 2;
    while (start >= 0)
    {
        sift_down(array, size, start, size - 1);
        start--;
    }

    /* Extract elements from heap one by one */
    end = size - 1;
    while (end > 0)
    {
        swap(&array[end], &array[0]);
        print_array(array, size);
        end--;
        sift_down(array, size, 0, end);
    }
}
