class Solution {
    public int minOperations(int[] nums, int x) {
        int t = Arrays.stream(nums).sum() - x;

        if (t == 0) {
            return nums.length;
        }

        int n = nums.length;
        int l = 0;
        int c = 0;
        int m = Integer.MAX_VALUE;

        for (int r = 0; r < n; r++) {
            c += nums[r];

            while (c > t && l <= r) {
                c -= nums[l];
                l += 1;
            }

            if (c == t) {
                m = Math.min(m, n - (r - l + 1));
            }
        }

        if (m == Integer.MAX_VALUE) {
            return -1;
        } else {
            return m;
        }
    }
}