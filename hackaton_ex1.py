from classiq import *
import matplotlib.pyplot as plt
from matplotlib import use
use('TkAgg')
@qfunc
def apply_condition(x: QNum, y: QBit):
    control(ctrl=(x == 2**20-1), stmt_block=lambda: X(y))
@qfunc
def main(x: Output[QNum],y: Output[QBit]):
    allocate(20,x)
    allocate(1,y)

    hadamard_transform(x)
    apply_condition(x,y)
    # control(ctrl=(x == 31), stmt_block=lambda: X(y))

depth_list = []
width_list = []
depth_prog_list = []

for ii in range(22,31):
    print(ii)
    quantum_model = create_model(main)

    quantum_model_with_constraints = set_constraints(
        quantum_model, Constraints(optimization_parameter="depth", max_width=ii)
    )
    quantum_program = synthesize(quantum_model_with_constraints)
    circuit_width = QuantumProgram.from_qprog(quantum_program).data.width
    circuit_depth = QuantumProgram.from_qprog(quantum_program).transpiled_circuit.depth
    program_depth = QuantumProgram.from_qprog(quantum_program).program_circuit.depth
    depth_prog_list.append(program_depth)
    depth_list.append(circuit_depth)
    width_list.append(circuit_width)

plt.figure()
plt.plot(width_list,depth_list, label='transpiled depth')
plt.plot(width_list,depth_prog_list, label='program depth')
plt.xlabel('width')
plt.ylabel('depth')
plt.title('20 qubit CX')
plt.legend()
plt.show()
# show(quantum_program)

