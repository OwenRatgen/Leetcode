public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        // 1. Create two count vars for common elements
        // 2. Loop through nums1 and keep track of how many ints are common
        // 3. Do the same but for nums2
        // 4. Create a list and append 
        
        int count1 = 0;
        int count2 = 0;

        foreach (int num in nums1) {
            if (nums2.Contains(num)) {
                count1++;
            }
        }
        foreach (int num in nums2) {
            if (nums1.Contains(num)) {
                count2++;
            }
        }
        int[] res = {count1, count2};

        return res;
    }
}