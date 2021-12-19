import sys

from solving.puzzle import Puzzle
from solving.solver import Solver
from words.dictionary import Dictionary
from words.word import Word
from interactive import Interactive
from time import perf_counter


def main():
    if len(sys.argv) > 2:
        solve(sys.argv[1:])
    else:
        Interactive(sys.argv[1:]).run()


def solve(args):
    first = args[0]
    second = args[1]
    if len(second) != len(first):
        print('Start word \'%s\' and end word \'%s\' not the same length!' % (first, second))
        sys.exit(-1)
    start = perf_counter()
    dictionary = Dictionary(len(first))
    took = (perf_counter() - start) * 1000
    print('Took %.2fms to load dictionary' % took)
    start_word: Word = dictionary[first]
    if start_word is None:
        print('Start word \'%s\' not in dictionary' % first)
        sys.exit(-1)
    elif start_word.is_island:
        print('Start word \'%s\' is an island word' % first)
        sys.exit(-1)
    end_word: Word = dictionary[second]
    if end_word is None:
        print('End word \'%s\' not in dictionary' % second)
        sys.exit(-1)
    elif end_word.is_island:
        print('End word \'%s\' is an island word' % second)
        sys.exit(-1)

    puzzle: Puzzle = Puzzle(start_word, end_word)
    max_ladder_length: int = -1
    if len(args) > 2:
        try:
            max_ladder_length = int(args[2])
            if max_ladder_length < 1:
                raise ValueError
        except ValueError:
            print('Max ladder length arg must be an integer (greater than zero)')
            sys.exit(-1)
    else:
        start = perf_counter()
        min_ladder = puzzle.calculate_minimum_ladder_length()
        took = (perf_counter() - start) * 1000
        if min_ladder is None:
            print('Cannot solve \'%s\' to \'%s\'' % (first, second))
            sys.exit(-1)
        max_ladder_length = min_ladder
        print('Took %.2fms to determine minimum ladder length of %d' % (took, max_ladder_length))

    solver = Solver(puzzle)
    start = perf_counter()
    solutions = solver.solve(max_ladder_length)
    took = (perf_counter() - start) * 1000
    if len(solutions) == 0:
        print('Cannot solve \'%s\' to \'%s\' in ladder length %d (took %.2fms)' % (first, second, max_ladder_length, took))
        sys.exit(-1)
    slen = len(solutions)
    print('Took %.2fms to find %d solutions (explored %d solutions)' % (took, slen, solver.explored_count))
    solutions.sort()
    for i in range(slen):
        print('%d/%d %s' % (i + 1, slen, solutions[i]))


if __name__ == '__main__':
    main()
