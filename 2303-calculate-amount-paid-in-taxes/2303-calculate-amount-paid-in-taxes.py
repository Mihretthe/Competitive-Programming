class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        lower_bound = 0
        for upper_bound, rate in brackets:
            if income <= lower_bound:
                break
            taxable_income = min(income - lower_bound, upper_bound - lower_bound)
            tax += taxable_income * rate / 100
            lower_bound = upper_bound
        return tax