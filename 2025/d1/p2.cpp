#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

    ifstream file("input.txt");

    int init = 50;
    int res = 0;

    string line;
    while (getline(file, line)){
        char dir = line[0];
        int steps = stoi(line.substr(1));
        int prev = init;

        if (dir == 'R'){
            init = ((prev + steps) % 100 + 100) % 100;
            res += (prev + steps) / 100;
        }
        else if (dir == 'L'){
            init = ((prev - steps) % 100 + 100) % 100;
            if (prev == 0) res += steps / 100;
            else res += ((100 - prev) + steps ) / 100;
        }

    }
    file.close();   
    cout << res << endl;

    return 0;
}