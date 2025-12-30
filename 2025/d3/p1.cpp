#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ifstream file("input.txt");

    int res = 0;
    string s;

    while (getline(file, s)) {

        s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());

        string left = s.substr(0, s.size() - 1);
        char max1 = *max_element(left.begin(), left.end());

        size_t i = left.find(max1);

        char max2 = *max_element(s.begin() + i + 1, s.end());
        res += (max1 - '0') * 10 + (max2 - '0'); // passer de ascii a int
    }
    
    cout << res << '\n';
    return 0;
}