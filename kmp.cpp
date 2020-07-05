#pragma once
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;

class Kmp {
private:
	const string str1, str2;
	int index = 0;

public:
	Kmp(const string &s1, const string &s2) :str1(s1), str2(s2) { }
	vector<int> get_next()		// 获取每个位置的最长前缀和最长后缀匹配长度
	{
		// 规定next[0]=-1, next[1]=0
		vector<int> next;
		next.push_back(-1);
		if (str2.length() == 1)
			return next;
		next.push_back(0);
		if (str2.length() == 2)
			return next;
		for (int j = 2; j < str2.length(); j++) {
			if (str2[j - 1] == str2[next[j - 1]]) {
				next.push_back(next[j - 1] + 1);
			}
			else {
				int i = next[j - 1];
				while (i > 1) {
					if (str2[j - 1] == str2[next[i]]) {
						next.push_back(next[i] + 1);
						break;
					}
					i = next[i - 1];
				}
			}
			if (next.size() == j + 1)
				continue;
			next.push_back(0);
		}
		return next;
	}
	int get_substr()			// 获取str2在str1中开始的位置
	{
		vector<int> next = get_next();
		int i = 0;
		for (i; i < str1.length(); ) {
			if (index == str2.length())
				return i - index;
			if (str1[i] == str2[index]) {
				i++;
				index++;
			}
			else {
				if (index < 2) {
					i++;
				}
				else
					index = next[index];
			}
		}
		return -1;
	}
};
