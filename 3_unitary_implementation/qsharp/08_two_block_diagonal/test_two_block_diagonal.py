from math import cos, pi, sin
from random import randint, random
import pytest
import qsharp
from qsharp.utils import dump_operation

def run_test_apply_two_block_diagonal(n, a, b):
  # For this version of the project, only test with 2 and 3 qubits.
  if n < 2 or n > 3:
    raise NotImplementedError("This test should run on 2- or 3-qubit unitaries")

  qsharp.init(project_root='.')
  matrix = dump_operation(f"UnitaryImplementation.ApplyTwoBlockDiagonal(_, {a}, {b})", n)

  zeros = [0] * 2 ** (n - 1)
  complete_coef = [a_row + zeros for a_row in a] + \
                  [zeros + b_row for b_row in b]

  for actual, expected in zip(matrix, complete_coef):
    assert actual == pytest.approx(expected, abs=1e-6)


def random_one_qubit_unitary():
  theta = random() * 2 * pi
  sign = +1 if randint(0, 1) == 1 else -1
  return [[cos(theta), sign * sin(theta)], 
         [-sin(theta), sign * cos(theta)]]

def test_two_qubit_two_block_diagonal():
  # Test on 2-qubit matrices (with 2x2 a and b).
  for j in range(1, 20):
    a = random_one_qubit_unitary()
    b = random_one_qubit_unitary()
    run_test_apply_two_block_diagonal(2, a, b)

def random_two_qubit_block_unitary():
  a = random_one_qubit_unitary()
  b = random_one_qubit_unitary()
  zeros = [0.0, 0.0]
  if randint(0, 1) == 1:
    return [a[0] + zeros, a[1] + zeros, zeros + b[0], zeros + b[1]]
  return [zeros + a[0], zeros + a[1], b[0] + zeros, b[1] + zeros]

def test_three_qubit_two_block_diagonal():
  # Test on 3-qubit matrices (with 4x4 a and b
  # of block-diagonal or anti-block-diagonal shape).
  for _ in range(1, 20):
    a = random_two_qubit_block_unitary()
    b = random_two_qubit_block_unitary()
    run_test_apply_two_block_diagonal(3, a, b)
