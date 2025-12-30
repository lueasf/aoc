#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool repet(long long nb) {
    string s = to_string(nb);
    int n = s.length();
    for (int i = 2; i <= n; ++i) {
        if (n % i != 0) continue;
        int part = n / i;
        string motif = s.substr(0, part);
        string repete = "";
        for (int k = 0; k < i; ++k) repete += motif;
        if (repete == s) return true;
    }
    return false;
}

int main() {
    ifstream file("input.txt");
    vector<pair<long long, long long>> ranges;
    stringstream buffer;
    buffer << file.rdbuf();
    string content = buffer.str();
    for (char& c : content) if (c == '\n') c = ',';
    stringstream ss(content);
    string part;
    
    while (getline(ss, part, ',')) {
        if (part.empty()) continue;
        int pos = part.find('-');
        long long start = stoll(part.substr(0, pos));
        long long end = stoll(part.substr(pos + 1));
        ranges.push_back({start, end});
    }
    long long res = 0;
    for (auto& range : ranges) {
        for (long long j = range.first; j <= range.second; ++j) {
            if (repet(j)) res += j;
        }
    }
    file.close();
    cout << res << endl;
    return 0;
}