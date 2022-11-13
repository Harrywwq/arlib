"""
FIXME: the file is very likely buggy
"""
import multiprocessing
import concurrent.futures
from typing import List, Tuple

import z3

from arlib.utils.exceptions import ForAllSolverSuccess


def check_candidate(fml: List[z3.BoolRef], fml_ctx: z3.Context):
    """
    Check candidate provided by the ExistsSolver
    :param fml: the formula to be checked
    :param fml_ctx: context of the fml
    :return A model in the origin_ctx
    """
    # print("Checking one ...", fml)
    solver = z3.SolverFor("QF_BV", ctx=fml_ctx)
    solver.add(fml)
    if solver.check() == z3.sat:
        m = solver.model()
        # will the next line cause race?
        return m  # to the original context?
    else:
        raise ForAllSolverSuccess()


def parallel_check_candidates(fmls: List[z3.BoolRef], num_workers: int):
    # Create new context for the computation
    # Note that we need to do this sequentially, as parallel access to the current context or its objects
    # will result in a segfault
    # origin_ctx = fmls[0].ctx
    tasks = []
    for fml in fmls:
        # tasks.append((fml, main_ctx()))
        i_context = z3.Context()
        i_fml = fml.translate(i_context)
        tasks.append((i_fml, i_context))

    # TODO: try processes?
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        #  with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(check_candidate, task[0], task[1]) for task in tasks]
        results = [f.result() for f in futures]
        return results


def parallel_check_candidates_multiprocessing(fmls: List[z3.ExprRef], num_workers):
    """Solve clauses under a set of assumptions (deal with each one in parallel)
    FIXME: ValueError: ctypes objects containing pointers cannot be pickled
    """
    assert num_workers >= 1
    tasks = []
    for fml in fmls:
        # tasks.append((fml, main_ctx()))
        i_context = z3.Context()
        i_fml = fml.translate(i_context)
        tasks.append((i_fml, i_context))

    answers_async = [None for _ in fmls]
    with multiprocessing.Pool(num_workers) as p:
        def terminate_others(val):
            if val:
                p.terminate()  # TODO: when do we need this?

        for i, task in enumerate(tasks):
            answers_async[i] = p.apply_async(
                check_candidate,
                (
                    task[0], task[1]
                ),
                callback=lambda val: terminate_others(val[0]))
        p.close()
        p.join()

    answers = [answer_async.get() for answer_async in answers_async if answer_async.ready()]
    res = [pres for pans, pres in answers]
    return res
