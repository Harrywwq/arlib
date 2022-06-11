import time
import multiprocessing
from multiprocessing import cpu_count
import pickle
import argparse
import os
import random

"""
thread pool
process pool
"""

def generate_data():
    return [random.randint(-100, 100) for _ in range(100)]


def sample_boolean_models(data):
    return random.sample(data, 20)


def boolean_solve(data, sample_number, pool, bool_term_queue):
    start = time.perf_counter()
    if random.random() < 0.01:
        # The Boolean Abstraction is UNSAT
        print("Boolean solver success")
        bool_term_queue.put(True)
        return []  # ?

    # Sample n Boolean models (specified by sample_number)
    results = []
    for i in range(sample_number):
        result = pool.apply_async(sample_boolean_models, (data,))
        results.append(result)

    boolean_models = []
    for i in range(0, sample_number):
        boolean_models.append(results[i].get())

    end = time.perf_counter()
    phase1_time = end - start
    print("PHASE 1 time：{}sec".format(phase1_time))
    return boolean_models


def check_theory_consistency(model, theory_term_queue):
    # the Boolean model is T-consistency
    # (thus, original formula is satisfiable)
    if sum(model) >= 1000:
        print("Theory solver success")
        theory_term_queue.put(True)

    return random.randint(0, 2)


def theory_solve(models, pool, theory_term_queue):
    start = time.perf_counter()
    results = []
    for i in range(len(models)):
        result = pool.apply_async(check_theory_consistency, (models[i], theory_term_queue,))  # 异步并行计算
        results.append(result)

    theory_res = []
    for i in range(len(models)):
        result = results[i].get()
        theory_res.append(result)
    end = time.perf_counter()
    phase2_time = end - start
    print("PHASE 2 time：{}sec".format(phase2_time))
    return theory_res


def main():
    formula = generate_data()  # A fake "SMT formula"
    boolean_abs = formula  # FIXME: should compute the Boolean abstraction

    sample_number = 10  # number of sampled Boolean models per round
    bool_term_queue = multiprocessing.Manager().Queue()  # flag for termination
    theory_term_queue = multiprocessing.Manager().Queue()  # flag for termination
    pool = multiprocessing.Pool(processes=cpu_count())  # process pool

    tried_number = 0
    while True:
        print("PHASE 1 (Boolean reasoning)...")
        boolean_models = boolean_solve(boolean_abs, sample_number, pool, bool_term_queue)

        print("PHASE 2 (Theory reasoning)...")
        theory_res = theory_solve(boolean_models, pool, theory_term_queue)

        # boolean_solve and theory_solve call pool.apply_async
        # So, the tasks in phase 2 may not be finished when calling this?
        if not (bool_term_queue.empty() and theory_term_queue.empty()):
            print("Either bool and theory solver success!")
            break

        # TODO: theory_res should refine boolean_abs

        tried_number += 1
        if tried_number >= 100:
            print("tried more than 100 times")
            break

    pool.close()
    pool.join()
    # print("Tried times: ", tried_number)


if __name__ == '__main__':
    main()
