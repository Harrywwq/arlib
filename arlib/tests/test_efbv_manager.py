# coding: utf-8
"""
For testing CDCL(T)-based parallel SMT solving engine
"""

import logging

import z3

from arlib.tests import TestCase, main
from arlib.tests.formula_generator import FormulaGenerator
from arlib.efsmt.efbv.efbv_utils import EFBVResult
from arlib.efsmt.efbv.efbv_to_bool import EFBVFormulaTranslator


def gen_small_bv_formula(logic: str):
    assert logic == "bv"
    x, y = z3.BitVecs("x y", 2)
    fg = FormulaGenerator([x, y])
    fml = fg.generate_formula()
    existential_vars = [x]
    universal_vars = [y]
    return existential_vars, universal_vars, fml


def is_simple_formula(fml: z3.ExprRef):
    # for pruning sample formulas that can be solved by the pre-processing
    clauses = z3.Then('simplify', 'elim-uncnstr', 'solve-eqs', 'tseitin-cnf')(fml)
    after_simp = clauses.as_expr()
    if z3.is_false(after_simp) or z3.is_true(after_simp):
        return True
    return False


def solve_with_z3(fml):
    sol = z3.Solver()
    sol.add(fml)
    res = sol.check()
    if res == z3.sat:
        return EFBVResult.SAT
    elif res == z3.unsat:
        return EFBVResult.UNSAT
    else:
        return EFBVResult.UNKNOWN


class TestEFBVManager(TestCase):

    def test_efbv_manager(self):
        from z3.z3util import get_vars
        # logging.basicConfig(level=logging.DEBUG)

        for _ in range(20):
            existential_vars, universal_vars, fml = gen_small_bv_formula("bv")
            vars_fml = [str(v) for v in get_vars(fml)]
            if not ("x" in vars_fml and "y" in vars_fml):
                continue
            if is_simple_formula(fml):
                continue

            fml_manager = EFBVFormulaTranslator()

            qbf = fml_manager.to_qbf(fml, existential_vars, universal_vars)
            solve_with_z3(qbf)


if __name__ == '__main__':
    main()
