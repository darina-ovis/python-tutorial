from typing import List

from kata.email import email_check
import codewars_test as test


@test.describe('email format verification')
def tests():
    @test.it('Test has @')
    def test_has_amp():
        given = "awdkhksahd@gmail.com"
        test.assert_equals(email_check(given), True)
        test.assert_equals(email_check("sdsayhdwghghy.ddd"), False)

    @test.it('Test has @')
    def test_has_point_and_2_symbols():
        given = "awdkhksahd@gmail.vla"
        test.assert_equals(email_check(given) , True)
