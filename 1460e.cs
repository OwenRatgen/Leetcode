public class Solution {
    public bool CanBeEqual(int[] target, int[] arr) {
        if (target == arr) {
            return true;
        }
        Array.Sort(arr);
        Array.Sort(target);
        for (int i = 0; i < target.Length; i++) {
            if (target[i] != arr[i]) {
                return false;
            }
        }
        return true;
    }
}