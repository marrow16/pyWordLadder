import unittest

from solving.puzzle import Puzzle
from solving.solver import Solver
from words.dictionary import Dictionary


class SolverTestCase(unittest.TestCase):
    def test_solve_cat_2_dog(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        dog = dictionary['dog']
        solver = Solver(Puzzle(cat, dog))

        solutions = solver.solve(4)
        self.assertEqual(4, len(solutions))
        self.assertEqual(38, solver.explored_count)

        mid_words: dict[str:int] = {}
        for solution in solutions:
            self.assertEqual(4, len(solution))
            self.assertEqual('CAT', str(solution[0]))
            self.assertEqual('DOG', str(solution[3]))
            mid_words[str(solution[1])] = 1 if str(solution[1]) not in mid_words else mid_words[str(solution[1])] + 1
            mid_words[str(solution[2])] = 1 if str(solution[2]) not in mid_words else mid_words[str(solution[2])] + 1
        self.assertEqual(5, len(mid_words))
        self.assertEqual(2, mid_words.get('CAG'))
        self.assertEqual(2, mid_words.get('COG'))
        self.assertEqual(2, mid_words.get('COT'))
        self.assertEqual(1, mid_words.get('DAG'))
        self.assertEqual(1, mid_words.get('DOT'))

    def test_solve_cold_2_warm_and_warm_2_cold(self):
        dictionary = Dictionary(4)
        cold = dictionary['cold']
        warm = dictionary['warm']
        solver = Solver(Puzzle(cold, warm))

        solutions = solver.solve(5)
        self.assertEqual(7, len(solutions))
        self.assertEqual(33, solver.explored_count)
        # now do it the other way around...
        solver = Solver(Puzzle(warm, cold))
        solutions = solver.solve(5)
        self.assertEqual(7, len(solutions))
        self.assertEqual(33, solver.explored_count)

    def test_solve_kata_2_java(self):
        dictionary = Dictionary(4)
        kata = dictionary['kata']
        java = dictionary['java']
        solver = Solver(Puzzle(kata, java))
        solutions = solver.solve(3)
        self.assertEqual(1, len(solutions))
        self.assertEqual('KATA', str(solutions[0][0]))
        self.assertEqual('KAVA', str(solutions[0][1]))
        self.assertEqual('JAVA', str(solutions[0][2]))

    def test_same_word_solvable(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        solver = Solver(Puzzle(cat, cat))
        solutions = solver.solve(1)
        self.assertEqual(1, len(solutions))
        self.assertEqual(0, solver.explored_count)

    def test_one_letter_difference_solvable(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        cot = dictionary['cot']
        solver = Solver(Puzzle(cat, cot))
        solutions = solver.solve(2)
        self.assertEqual(1, len(solutions))
        self.assertEqual(0, solver.explored_count)

    def test_two_letters_difference_solvable(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        bar = dictionary['bar']
        solver = Solver(Puzzle(cat, bar))
        solutions = solver.solve(3)
        self.assertEqual(2, len(solutions))
        self.assertEqual(0, solver.explored_count)

    def test_everything_unsolvable_with_bad_max_ladder_length(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        dog = dictionary['dog']
        solver = Solver(Puzzle(cat, dog))
        solutions = solver.solve(-1)
        self.assertEqual(0, len(solutions))
        solutions = solver.solve(0)
        self.assertEqual(0, len(solutions))
        solutions = solver.solve(1)
        self.assertEqual(0, len(solutions))
        solutions = solver.solve(2)
        self.assertEqual(0, len(solutions))
        solutions = solver.solve(3)
        self.assertEqual(0, len(solutions))
        solutions = solver.solve(4)
        self.assertTrue(len(solutions) > 0)

    def test_short_circuit_on_one_letter_difference(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        cot = dictionary['cot']
        solver = Solver(Puzzle(cat, cot))
        solutions = solver.solve(3)
        self.assertEqual(3, len(solutions))
        self.assertEqual(0, solver.explored_count)


if __name__ == '__main__':
    unittest.main()
