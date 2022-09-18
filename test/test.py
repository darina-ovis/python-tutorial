from typing import List

from kata.solution import final_value_after_operations
import codewars_test as test
# Leetcode #2011. Final Value of Variable After Performing Operations


@test.describe('Final Value of Variable After Performing Operations Tests')
def tests():
    @test.it('Example 1 Test Case')
    def example_test_case():
        given: List[str] = ["X++", "++X", "--X", "X--"]
        test.assert_equals(final_value_after_operations(given), 0)

    @test.it('Example 2 Test Case')
    def example_test_case():
        given: List[str] = ["--X", "X++", "X++"]
        test.assert_equals(final_value_after_operations(given), 1, 'Total is invalid')
