class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int t = accumulate(nums.begin(), nums.end(), 0) - x;

        if (t == 0) {
            return nums.size();
        }

        int n = nums.size();
        int l = 0;
        int c = 0;
        int m = INT_MAX;

        for (int r = 0; r < n; r++) {
            c += nums[r];

            while (c > t && l <= r) {
                c -= nums[l];
                l += 1;
            }

            if (c == t) {
                m = min(m, n - (r - l + 1));
            }
        }

        if (m == INT_MAX) {
            return -1;
        } else {
            return m;
        }
    }
};