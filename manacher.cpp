class Solution {
public:
    vector<int> radi = {0}; // radi数组记录每个位置为的回文半径
    int C = 0, R = 0;       // C是最大回文半径中心，R是回文有边界

    string reshape(string str){
        int len = str.length();
        for (int i = 0; i != len; i++)
            str.insert(2 * i, "#");
        str.append("#");
        return str;
    }

    string longestPalindrome(string s) {
        string str = reshape(s);
        string ans;
        for (int i = 0; i != str.length(); i++) {
            if (i < R) {
                int cur_R = (R - i) > radi[2 * C - i] ? radi[2 * C - i] : (R - i);
                radi[i] = cur_R;
            }
            else
                radi[i] = 1;
            while (i >= radi[i] && i + radi[i] < str.length() && str[i + radi[i]] == str[i - radi[i]]) {
                radi[i]++;
            }
            if (radi[i] + i - 1 > R) {
                R = radi[i] + i - 1;
                C = i;
            }
            R = R > radi[i] ? R : radi[i];
            radi.push_back(0);
        }
        vector<int>::iterator big = max_element(begin(radi), end(radi));
        int index = distance(begin(radi), big);
        for (int i = index - (*big) + 1; i < index + (*big) - 1; i++) {
            if (str[i] == '#')
                continue;
            ans.insert(ans.end(),str[i]);
	    }
        return ans;
    }

    
};
