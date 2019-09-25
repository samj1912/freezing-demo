#cython: language_level=3
import another_process
def print_process():
    print("Process here! Nice to meet you!")
    another_process.print_process()
