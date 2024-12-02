﻿operation ReadInformation(qs : Qubit[]) : Result[] {
  mutable res = [];
  for q in qs {
    set res += [MResetZ(q)];
  }
  return res;
}
