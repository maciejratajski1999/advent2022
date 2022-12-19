#include <iostream>
#include <fstream>
#include <vector>
#include <map>

template<typename T>
void printVector(std::vector<T> v){
    for (T i : v) std::cout << i << ", ";
    std::cout << std::endl;
}
auto sum = [](std::vector<int> v) {
    int accumulator = 0;
    for (int i : v) {
        accumulator = accumulator + i;
    }
    return accumulator;
};

std::string readLine(std::fstream &file){
    std::string line;
    std::getline(file, line);
    return line;
}
std::vector<std::string> splitLine(std::string line, char d){
    std::vector<std::string> lineVector;
    std::string temp;
    for (char c : line){
        if (c==d) {
            lineVector.push_back(temp);
            temp="";
        }
        else temp = temp + c;
    }
    lineVector.push_back(temp);
    return lineVector;
}

int getOrder(std::string line){
    std::vector<std::string> lineVector = splitLine(line, ' ');
    if (lineVector[0]=="noop") return 0;
    else if (lineVector[0]=="addx") return std::stoi(lineVector[1]);
    else return NULL;
}
std::vector<int> getOrders(std::string filename){
    std::fstream file;
    file.open(filename, std::ios_base::in);
    std::vector<int> orders;
    while (!file.eof()){
        //use of & reference
        std::string line = readLine(file);
        int registerValue = getOrder(line);
        orders.push_back(registerValue);
    }
    file.close();
    return orders;
}

int sumRegister(std::vector<int> orders){ return sum(orders); }
std::map<int, int> mapRegisterValues(std::vector<int> orders){
    std::map<int, int> values;
    int cycle = 0;
    int value = 1;
    for (int order : orders){
        values[cycle] = value;
        std::cout << ++cycle << " the cycle started, X: " << value << std::endl;
        if (order==0) {
            std::cout << "noop " << std::endl;
        }
        else {
            values[cycle] = value;
            ++cycle;
            value = value + order;
            std::cout << "addx " << order << std::endl;
        }
    }
    return values;
}
void drawCRT(std::map<int, int> registerValues){
    for (std::pair<int, int> state : registerValues){
        int pixel = state.first % 40;
        if (pixel == 0) std::cout << state.first << std::endl;
        char lit = abs(pixel - state.second) <= 1 ? '#' : '.';
        std::cout << lit;
    }
}
int main() {
    std::vector orders = getOrders("input.txt");
//    printVector(orders);
    std::map<int, int> registerValues = mapRegisterValues(orders);
    std::vector<int> valuesAtCycle;
    for (int cycle : {19, 59, 99, 139, 179, 219}) valuesAtCycle.push_back(registerValues[cycle] * (cycle+1));
    printVector(valuesAtCycle);
    std::cout << sum(valuesAtCycle) << std::endl;
    drawCRT(registerValues);
    return 0;
}
