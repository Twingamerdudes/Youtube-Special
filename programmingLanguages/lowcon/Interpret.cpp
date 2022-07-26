#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using namespace std::literals::chrono_literals;
auto start = std::chrono::high_resolution_clock::now();
bool contains(std::string str, std::string substr) {
    if (str.find(substr) != std::string::npos) {
        return true;
    }
    return false;
}
void Interpret(string line, int lineNumber) {
    if (contains(line, "print")) {
        cout << line.substr(line.find_first_of("\"") + 1, line.find_last_of("\"") - 8);
    }
    if (contains(line, "endline")) {
        cout << "\n";
    }
    if (contains(line, "end")) {
        exit(0);
    }
}
