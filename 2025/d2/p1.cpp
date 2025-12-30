#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool repet(int nb) {
    string s = to_string(nb);
    int n = s.length();
    if (n % 2 != 0) return false;
    int half = n / 2;
    return s.substr(0, half) == s.substr(half);
}

int main() {

    ifstream file("test.txt");
    
    stringstream buffer;
    buffer << file.rdbuf();
    string content = buffer.str();
    
    for (int i = 0; i < content.size(); i++) {
        if (content[i] == '\n') content[i] = ',';
    }
    
    vector<pair<int, int>> ranges;
    stringstream ss(content);
    string part;
    while (getline(ss, part, ',')) {
        if (part.empty()) continue;
        int pos = part.find('-');
        int start = stoi(part.substr(0, pos));
        int end = stoi(part.substr(pos + 1));
        ranges.push_back({start, end});
    }
    
    int res = 0;
    for (auto& range : ranges) {
        for (int j = range.first; j <= range.second; j++) {
            if (repet(j)) {
                res += j;
            }
        }
    }
    
    file.close();
    cout << res << endl;
    
    return 0;
}