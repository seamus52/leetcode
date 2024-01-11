public class Solution {
    public void Transpose(int[][] m) {
        for (int r = 0; r < m.Length; r++) {
            for (int c = r; c < m.Length; c++) {
                (m[r][c], m[c][r]) = (m[c][r], m[r][c]);
            }
        }
    }

    public void Mirror(int[][] m) {
        for (int r = 0; r < m.Length; r++) {
            for (int c = 0; c < m.Length / 2; c++) {
                (m[r][c], m[r][m.Length - c - 1]) = (m[r][m.Length - c - 1], m[r][c]);
            }
        }
    }

    public void Rotate(int[][] m) {
        Transpose(m);
        Mirror(m);
    }
}
