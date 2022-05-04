from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCAABBD") == 240

    def test_checkout_invalid_input(self):
        assert checkout_solution.checkout("ABCAABBDa") == -1
