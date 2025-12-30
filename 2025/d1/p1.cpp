#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

    ifstream file("test.txt");

    int init = 50;
    int res = 0;

    string line;
    while (getline(file, line)){
        char dir = line[0];
        int steps = stoi(line.substr(1));

        if (dir == 'R'){
            init = (init + steps) % 100;
            if (init == 0) res ++;
        }
        else if (dir == 'L'){
            init = (init - steps) % 100;
            if (init == 0) res ++;
        }

    }
    file.close();   
    cout << res << endl;

    return 0;
}