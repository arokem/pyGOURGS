import sys, os
sys.path.append(os.path.join('.', 'pyGOURGS'))
import pyGOURGS.pyGOURGS as pg
from pyGOURGS.pyGOURGS import decimal_to_base_m, base_m_to_decimal
import unittest
from operator import add, sub, truediv, mul

class TestNumberBaseConversions(unittest.TestCase):

    def test_base_one(self):
        self.assertEqual(decimal_to_base_m(5,1), [1,1,1,1,1])
        self.assertEqual(base_m_to_decimal(11111,1), 5)
        self.assertEqual(base_m_to_decimal([1,1,1,1,1],1), 5)

    def test_base_two(self):
        self.assertEqual(decimal_to_base_m(5,2), [1,0,1])
        self.assertEqual(base_m_to_decimal(101,2), 5)
        self.assertEqual(base_m_to_decimal([1,0,1],2), 5)
        
    def test_base_three(self):
        self.assertEqual(decimal_to_base_m(125,3), [1,1,1,2,2])
        self.assertEqual(base_m_to_decimal(11122,3), 125)
        self.assertEqual(base_m_to_decimal([1,1,1,2,2],3), 125)
        
    def test_base_nine(self):
        self.assertEqual(decimal_to_base_m(125,9), [1,4,8])
        self.assertEqual(base_m_to_decimal(148,9), 125)
        self.assertEqual(base_m_to_decimal([1,4,8],9), 125)
        
    def test_base_25(self):
        self.assertEqual(125, base_m_to_decimal(decimal_to_base_m(
                                                125,25),25))
        self.assertEqual(183513434438, base_m_to_decimal(
                            decimal_to_base_m(183513434438,94),94))


class TestSymbolicRegression(unittest.TestCase):

    def setUp(self):
        self.pset = pg.PrimitiveSet()
        self.pset.add_operator(add, 2)
        self.pset.add_operator(sub, 1)
        self.pset.add_operator(truediv, 3)
        self.pset.add_operator(mul, 1)
        self.pset.add_variable(1)
        self.pset.add_variable(0)
        self.enum = pg.Enumerator(self.pset)

    def test_count_unique_trees(self):
        trees = list()
        N_trees = 20
        for i in range(0,N_trees):
            tree = self.enum.ith_n_ary_tree(i)
            trees.append(tree)
            print(tree)
        self.assertEqual(len(list(set(trees))), N_trees)

    def test_terminal(self):
        self.assertEqual(self.enum.ith_n_ary_tree(0), '..')

    def test_operator_1(self):
        self.assertEqual(self.enum.ith_n_ary_tree(1), '[..]')

    def test_operator_2(self):
        self.assertEqual(self.enum.ith_n_ary_tree(2), '[..,..]')

    def test_operator_3(self):
        self.assertEqual(self.enum.ith_n_ary_tree(3), '[..,..,..]')

    def test_count_operators_0(self):
        self.assertEqual(self.enum.calculate_l_i_b(0, 0), 0)

    def test_count_operators_0(self):
        self.assertEqual(self.enum.calculate_l_i_b(1, 0), 1)

    def test_count_operators_0(self):
        self.assertEqual(self.enum.calculate_l_i_b(2, 1), 1)
        self.assertEqual(self.enum.calculate_l_i_b(2, 0), 0)
        self.assertEqual(self.enum.calculate_l_i_b(1, 0), 1)
        self.assertEqual(self.enum.calculate_l_i_b(4, 0), 2)

    def test_count_total_configurations_operators_0(self):
        self.assertEqual(self.enum.calculate_G_i_b(4,0), 4)
        self.assertEqual(self.enum.calculate_G_i_b(11,0), 4)

    def test_count_total_configurations_all_arities_0(self):
        self.assertEqual(self.enum.calculate_R_i(0),1)
        self.assertEqual(self.enum.calculate_R_i(1),2)
        self.assertEqual(self.enum.calculate_R_i(2),1)
        self.assertEqual(self.enum.calculate_R_i(3),1)
        self.assertEqual(self.enum.calculate_R_i(11),4)

    def test_count_total_configurations_terminals_0(self):
        self.assertEqual(self.enum.calculate_a_i(0),1)
        self.assertEqual(self.enum.calculate_a_i(1),1)
        self.assertEqual(self.enum.calculate_a_i(2),2)
        self.assertEqual(self.enum.calculate_a_i(3),3)
        self.assertEqual(self.enum.calculate_a_i(4),1)
        self.assertEqual(self.enum.calculate_a_i(5),2)
        
    def test_count_total_configurations_terminals_0(self):
        self.assertEqual(self.enum.calculate_S_i(0),2)
        self.assertEqual(self.enum.calculate_S_i(1),2)
        self.assertEqual(self.enum.calculate_S_i(2),4)
        self.assertEqual(self.enum.calculate_S_i(3),8)
        self.assertEqual(self.enum.calculate_S_i(4),2)
        self.assertEqual(self.enum.calculate_S_i(5),4)

if __name__ == '__main__':
    unittest.main()

