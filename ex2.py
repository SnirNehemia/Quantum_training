from classiq import *


@qfunc
def apply_condition(index: CInt, qubit: QBit):
    if_(condition=index % 2 == 0, then=lambda: X(qubit))


@qfunc
def main(x: Output[QArray]):
    allocate(10, x)
    repeat(count=x.len, iteration=lambda index: apply_condition(index, x[index]))


quantum_program = synthesize(create_model(main))
show(quantum_program)

results = execute(quantum_program).result()[0].value
print(results.counts)

write_qmod(create_model(main), "classical_variables_and_operations")