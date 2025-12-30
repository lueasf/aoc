#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream file("test.txt");

    long long res = 0;
    string line;
    
    while (getline(file, line)) {
        line.erase(remove_if(line.begin(), line.end(), [](unsigned char c){ return isspace(c); }), line.end());

        string s = line;
        if (!all_of(s.begin(), s.end(), [](unsigned char c){ return isdigit(c); })) continue;
        int n = (int)s.size();

        vector<char> max_vars(12);
        vector<int> index_vars(12, -1);
        bool ok = true;

        for (int i = 0; i < 12; ++i) {
            int pos, end;
            if (i == 0) { pos = 0; end = n - 11; }
            else if (i < 11) { pos = index_vars[i-1] + 1; end = n - (11 - i); }
            else { pos = index_vars[i-1] + 1; end = n; }

            if (pos < 0 || pos >= n || end <= pos) { ok = false; break; }

            auto it = max_element(s.begin() + pos, s.begin() + end);
            char mv = *it;
            int idx = (int)s.find(mv, pos);
            if (idx == string::npos) { ok = false; break; }

            max_vars[i] = mv;
            index_vars[i] = idx;
        }

        if (!ok) continue;

        string num;
        num.reserve(12);
        for (char c : max_vars) num.push_back(c);
        res += stoll(num);
    }

    cout << res << '\n';
    return 0;
}