from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCAABBD") == 240

    def test_checkout_invalid_input(self):
        assert checkout_solution.checkout("ABCAABBDa") == -1

    def test_checkout_two_b_discount(self):
        assert checkout_solution.checkout("BB") == 45

    def test_checkout_three_a_discount(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout_five_a_discount(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_checkout_five_a_discount(self):
        assert checkout_solution.checkout("FFABCDECBAABCABBAAAEEAAFF") == 695
