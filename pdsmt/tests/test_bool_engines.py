# coding: utf-8
"""
The the Boolean-level reasoning engines in the parallel CDCL(T) engine
"""
from . import TestCase, main
# from ..theory import SMTLibTheorySolver, SMTLibPortfolioTheorySolver
# from ..global_params.paths import cvc5_exec, z3_exec
from .grammar_gene import gen_cnf_numeric_clauses
from ..bool.pysat_solver import PySATSolver


class TestBoolEngines(TestCase):

    def test_models_sampling_and_reducing(self):
        for _ in range(10):
            clauses = gen_cnf_numeric_clauses()
            if len(clauses) == 0:
                continue
            # solver_name = random.choice(sat_solvers)
            s = PySATSolver()
            s.add_clauses(clauses)
            if s.check_sat():
                print("SAT")
                models = s.sample_models(10)
                reduced_models = s.reduce_models(models)
                assert(len(models) <= len(reduced_models))
                break


if __name__ == '__main__':
    main()
