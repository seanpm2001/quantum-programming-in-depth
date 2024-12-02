import qsharp

def test_one_bit_phase_estimation():
  qsharp.init(project_root='.')
  qsharp.eval("Test.TestOneBitPhaseEstimation()")

def test_iterative_phase_estimation():
  qsharp.init(project_root='.')
  qsharp.eval("Test.TestIterativePhaseEstimation()")

def test_adaptive_phase_estimation():
  qsharp.init(project_root='.')
  qsharp.eval("Test.TestAdaptivePhaseEstimation()")

def test_quantum_phase_estimation():
  qsharp.init(project_root='.')
  qsharp.eval("Test.TestQuantumPhaseEstimation()")
