void Solution::arrange(vector<int> &A) {
    vector<int> B = A;
    for (int i = 0; i < A.size(); i ++) {
        A[i] += (A[A[i]] % A.size()) * A.size();
    }
    for (int i = 0; i < A.size(); i ++) {
        A[i] = A[i] / A.size();
    }
}
