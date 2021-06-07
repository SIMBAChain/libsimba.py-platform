import unittest 
from generated_simba_hinted_contract import Application

class TestSimbaOutput(unittest.TestCase):

    a = Application()

    def test_view_param_restrictions(self):
        # comment out this function to prevent printing of parameter restrictions
        print('parameter restrictions:')
        print(TestSimbaOutput.a.simba_contract.params_restricted)

    def test_fail_negative_array_input(self):
        # following should fail because elements must be uints
        arr1 = [-10,4,6,8]
        arr2 = [1,3,5,10]
        with self.assertRaises(ValueError):
            TestSimbaOutput.a.two_arrs(arr1, arr2)

    def test_fail_non_uint_input(self):
        # following should fail because this method's array params should only accept
        arr1 = [2, 4, 'hello', 10]
        arr2 = [1,3,5]
        with self.assertRaises(TypeError):
            TestSimbaOutput.a.two_arrs(arr1, arr2)

    def test_pass_unequal_lengths(self):
        # should pass - two_arrs does not have length requirements on arrays 
        arr1 = [2, 4, 20, 10, 3, 3]
        arr2 = [1,3,5]
        status_code = TestSimbaOutput.a.two_arrs(arr1, arr2).status_code
        self.assertEqual(status_code, 202)
    
    def test_fail_incorrect_outer_array_lengths(self):
        # should fail - nested_arr_3 must contain 3 arrays
        arr1 = [[1,2,3], [2,2,2]]
        with self.assertRaises(ValueError):
            TestSimbaOutput.a.nested_arr_3(arr1)

    def test_fail_incorrect_inner_array_lengths(self):
        # should fail - nested_arr_3's arrays must contain 3 elements
        arr1 = [[1,2,3], [99,99], [13,13,13]]
        with self.assertRaises(ValueError):
            TestSimbaOutput.a.nested_arr_3(arr1)

    def test_fail_mixed_element_data_types(self):
        # should fail - array element data types cannot be mixed in solidity
        arr1 = [[2,2,2], 'hello', [13,13,13]]
        with self.assertRaises(TypeError):
            TestSimbaOutput.a.nested_arr_3(arr1)

    def test_fail_too_many_dimensions(self):
        # should fail - too many dimensions
        arr1 = [1,2,3]
        arr2 = [[arr1,arr1,arr1], [arr1,arr1,arr1], [arr1,arr1,arr1]]
        with self.assertRaises(ValueError):
            TestSimbaOutput.a.nested_arr_3(arr2)

if __name__ == '__main__':
    unittest.main()