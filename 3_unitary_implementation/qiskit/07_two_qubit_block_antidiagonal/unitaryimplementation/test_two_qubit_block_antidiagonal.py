from math import cos, pi, sin
from random import randint, random
from qiskit.quantum_info import Operator
from pytest import approx
from .two_qubit_block_antidiagonal import apply_two_qubit_block_antidiagonal

def run_test_apply_two_qubit_block_antidiagonal(a, b):
  op = Operator(apply_two_qubit_block_antidiagonal(a, b))
  matrix = op.data

  complete_coef = [
      [0., 0.] + a[0],
      [0., 0.] + a[1],
      b[0] + [0., 0.],
      b[1] + [0., 0.]]

  for actual, expected in zip(matrix, complete_coef):
    assert actual == approx(expected)

def random_one_qubit_unitary():
  theta = random() * 2 * pi
  sign = +1 if randint(0, 1) == 1 else -1
  return [[cos(theta), sign * sin(theta)], 
         [-sin(theta), sign * cos(theta)]]

def test_two_qubit_block_diagonal():
  for _ in range(1, 20):
    a = random_one_qubit_unitary()
    b = random_one_qubit_unitary()
    run_test_apply_two_qubit_block_antidiagonal(a, b)
