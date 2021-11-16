from random import shuffle

def _swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

class SortObj:
    def __init__(self, arr, stdscr, redraw_func):
        self.arr = arr
        self.window = stdscr
        self.redraw_func = redraw_func
        self.sa = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Quick Sort": self.quick_sort
        }

    def shuffle(self):
        shuffle(self.arr)

    def sort_using(self, a_name):
        self.shuffle()
        self.redraw_func(self.window, self.arr)
        self.sa[a_name]()

    def _q_partition(self, lo, hi):
        i = lo
        j = hi
        while True:
            i += 1
            while self.arr[i] < self.arr[lo]:
                if i == hi: break
                i += 1
                self.redraw_func(self.window, self.arr, i)
            while self.arr[j] > self.arr[lo]:
                if j == lo: break
                j -= 1
                self.redraw_func(self.window, self.arr, j)
            if i >= j: break
            _swap(self.arr, i, j)
            self.redraw_func(self.window, self.arr, i)
        _swap(self.arr, lo, j)
        return j

    def _q_sort(self, lo, hi):
        if hi <= lo: return
        j = self._q_partition(lo, hi)
        self._q_sort(lo, j - 1)
        self._q_sort(j + 1, hi)

    def quick_sort(self):
        n = len(self.arr)
        self._q_sort(0, n - 1)

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    _swap(self.arr, j, j + 1)
                    self.redraw_func(self.window, self.arr, j + 1)

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if self.arr[min] > self.arr[j]:
                    min = j
                self.redraw_func(self.window, self.arr, j)
            _swap(self.arr, i, min)
