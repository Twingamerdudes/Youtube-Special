#include <iostream>
#include <fstream>
#include <string>
#include "Interpret.h"

using std::cout;
using std::endl;
using std::string;
int main()
{
    cout << "Please enter a file name" << endl;
    string name;
    std::getline(std::cin, name);
    std::ifstream file(name);
    string line;
    int i = 0;
    bool mainDefined = false;
    while (std::getline(file, line)) {
        i++;
        Interpret(line, i);
    }
    cout << "\n";
    cout << "ERORR: " << i << " PROGRAM DID NOT END" << endl;
    std::cin.ignore();
    exit(1);
    return 0;
}

