from classiq import *

""" exercise 1 """
# @qfunc
# def main(indicator: Output[QBit]):
#
#     x = QNum("x")
#     allocate(10, x)
#     repeat(len(x),)
#     flip_msb(x)
#
#     indicator |= x == 8
"""exercise 2 """
# @qfunc
# def apply_condition(index: CInt, qubit: QBit):
#     if_(condition=index % 2 == 0, then=lambda: X(qubit))

@qfunc
# def main(x: Output[QArray]):
#     allocate(10, x)
#     repeat(count=x.len, iteration=lambda index: apply_condition(index, x[index]))

""" control gate """


@qfunc
def apply_control(x: QNum, y: QNum):
    control(ctrl=(x == 15), stmt_block=(lambda: inplace_xor(17, y)))


""" optimization of circuit """
quantum_model = create_model(main)

quantum_model_with_constraints = set_constraints(
    quantum_model, Constraints(optimization_parameter="width", max_depth=500)
)



quantum_program = synthesize(create_model(main))
show(quantum_program)
# job = execute(quantum_program)
# results = job.result()[0].value.parsed_counts
# print(results)
