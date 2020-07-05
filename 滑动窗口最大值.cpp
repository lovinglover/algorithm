class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int R = 0, L = 0;
        deque<pair<int, int>> MAX;
        vector<int> ans;
        while(R != nums.size()){
            if(MAX.empty()) MAX.push_back(pair<int, int>(nums[R], R));
            else{
                if(nums[R] < MAX.back().first) MAX.push_back(pair<int, int>(nums[R], R));
                else{
                    while(!MAX.empty() && nums[R] >= MAX.back().first){
                        MAX.pop_back();
                    }
                    MAX.push_back(pair<int, int>(nums[R], R));
                }
            }
            if(R - L + 1 == k){
                ans.push_back(MAX.front().first);
                if(L >= MAX.front().second) MAX.pop_front();
                L++;
            }
            R++;
        }
        return ans;
    }
};
