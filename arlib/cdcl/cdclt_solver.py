"""
Interface for CDCL(T)-based Solver
"""
import itertools
from abc import ABC, abstractmethod
from arlib.cdcl.parallel_cdclt_process import parallel_cdclt_process
from arlib.cdcl.parallel_cdclt_thread import parallel_cdclt_thread
from arlib.utils import SolverResult


class CDCLSolver(ABC):
    """
    Abstract base class for a solver which implements the Conflict Driven Clause Learning (CDCL) algorithm for solving
    Satisfiability Modulo Theories (SMT) problems.
    """
    def __init__(self, **kwargs):
        self.seed = kwargs.get("seed", 1)

    @abstractmethod
    def solve_smt2_string(self, smt2string: str, logic: str) -> SolverResult:
        """
        Abstract method that solves an SMT-LIB2 problem with the CDCL algorithm.
        Parameters:
        -----------
        smt2string : str
            The SMT-LIB2 problem in its input format.
        logic : str
            The logic in use.
        Returns:
        --------
        SolverResult
            The result of the solver as a SolverResult object.
        """
        pass


class SequentialCDCLSolver(CDCLSolver):
    def __init__(self, **kwargs):
        self.seed = kwargs.get("seed", 1)

    def solve_smt2_string(self, smt2string: str, logic: str) -> SolverResult:
        pass


class ParallelCDCLSolver(CDCLSolver):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parallel_mode = kwargs.get("mode", "process")

    def solve_smt2_string(self, smt2string: str, logic: str) -> SolverResult:
        if self.parallel_mode == "process":
            return parallel_cdclt_process(smt2string, logic)
        elif self.parallel_mode == "thread":
            return parallel_cdclt_thread(smt2string, logic)
        else:
            return parallel_cdclt_process(smt2string, logic)
