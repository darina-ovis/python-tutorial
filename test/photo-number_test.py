from typing import List

from kata.solution import phone_number_verify
import codewars_test as test

# ['89112360136', '9112360136', '911-234-12-45', '71q23455678']
# 10 цифр первая 7 или 8, все числа
# [true, false, false, false]

@test.describe('Phone number format verification')
def tests():
    @test.it('Test exactly 10 chars')
    def test_exactly_ten():
        given: List[str] = ["8234567890", "1"]
        test.assert_equals(phone_number_verify(given), [True, False])

    @test.it('')
    def test_first_char():
        given: List[str] = ["8888888888", "7777777777", "1888888899"]
        test.assert_equals(phone_number_verify(given), [True, True, False])

    @test.it('')
    def test_all_digits():
        given: List[str] = ["8888888888", "7a7777d777"]
        test.assert_equals(phone_number_verify(given), [True, False])
