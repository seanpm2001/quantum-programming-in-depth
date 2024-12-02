﻿import Std.Arrays.*;

operation MultiAnd(x : Qubit[], y : Qubit) : Unit is Adj + Ctl {
  Controlled X(x, y);
}

operation MultiOr(x : Qubit[], y : Qubit) : Unit is Adj + Ctl {
  ApplyControlledOnInt(0, X, x, y);
  X(y);
}

operation EvaluateClause(x : Qubit[], y : Qubit, literals : (Int, Bool)[]) : Unit is Adj + Ctl {
  let controlQubits = Mapped((ind, _) -> x[ind], literals);
  let controlPattern = Mapped((_, pos) -> pos, literals);
  within {
    // Convert all literals to positive.
    ApplyPauliFromBitString(PauliX, false, controlPattern, controlQubits);
  } apply {
    // Calculate the OR of all literals.
    MultiOr(controlQubits, y);
  }
}

operation EvaluateExpression(x : Qubit[], y : Qubit, expression : (Int, Bool)[][]) : Unit is Adj + Ctl {
  let nClauses = Length(expression);
  use clauseResults = Qubit[nClauses];
  within {
    for (clause, result) in Zipped(expression, clauseResults) {
      EvaluateClause(x, result, clause);
    }
  } apply {
    // All clauses must be true
    MultiAnd(clauseResults, y);
  }
}
