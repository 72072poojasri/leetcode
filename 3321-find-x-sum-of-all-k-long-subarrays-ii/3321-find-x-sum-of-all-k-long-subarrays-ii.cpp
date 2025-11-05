#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        unordered_map<int,int> freq;
        multiset<pair<int,int>> top, rest; // pairs = (-freq, -val)
        long long topSum = 0;
        vector<long long> res;

        auto balance_after_insert_remove = [&](void){
            // ensure top has up to x best elements
            while ((int)top.size() < x && !rest.empty()) {
                auto move = *rest.begin();
                rest.erase(rest.begin());
                top.insert(move);
                long long f = -move.first;
                long long v = -move.second;
                topSum += f * v;
            }
            if (!rest.empty() && !top.empty() && *rest.begin() < *top.rbegin()) {
                auto moveOut = *top.rbegin();
                auto moveIn = *rest.begin();
                top.erase(prev(top.end()));
                rest.erase(rest.begin());
                // swap
                rest.insert(moveOut);
                top.insert(moveIn);
                long long outF = -moveOut.first;
                long long outV = -moveOut.second;
                long long inF = -moveIn.first;
                long long inV = -moveIn.second;
                topSum += inF * inV - outF * outV;
            }
        };

        auto add = [&](int num) {
            int f = freq[num];
            if (f > 0) {
                pair<int,int> oldp = {-f, -num};
                auto itTop = top.find(oldp);
                if (itTop != top.end()) {
                    top.erase(itTop);
                    topSum -= 1LL * f * num;
                } else {
                    auto itRest = rest.find(oldp);
                    if (itRest != rest.end()) rest.erase(itRest);
                }
            }
            freq[num]++;
            rest.insert({-freq[num], -num});
            balance_after_insert_remove();
        };

        auto remove = [&](int num) {
            int f = freq[num];
            if (f == 0) return;
            pair<int,int> oldp = {-f, -num};
            auto itTop = top.find(oldp);
            if (itTop != top.end()) {
                top.erase(itTop);
                topSum -= 1LL * f * num;
            } else {
                auto itRest = rest.find(oldp);
                if (itRest != rest.end()) rest.erase(itRest);
            }
            freq[num]--;
            if (freq[num] > 0) rest.insert({-freq[num], -num});
            balance_after_insert_remove();
        };

        // initialize window
        for (int i = 0; i < k; ++i) add(nums[i]);
        res.push_back(topSum);

        // slide window
        for (int i = k; i < n; ++i) {
            remove(nums[i - k]);
            add(nums[i]);
            res.push_back(topSum);
        }
        return res;
    }
};