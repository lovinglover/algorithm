class Solution {
public:
	string replaceSpaces(string S, int length) {
        int count = 0;
        for(int i = 0; i < length; i++){
            if(S[i] == ' ') count++;
        }
        int new_len = length + count * 2, tail = new_len - 1;
        for(int i = length - 1; i >= 0; i--){
            if(S[i] == ' '){
                S[tail--] = '0';
                S[tail--] = '2';
                S[tail--] = '%';
            }
            else
                S[tail--] = S[i];
            S[new_len] = '\0';
        }
        return S;
	}
};
