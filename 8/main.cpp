#include <iostream>
#include <fstream>
#include <vector>
std::string readLine(std::fstream &file){
    std::string line;
    std::getline(file, line);
    return line;
}

std::vector<int> toDigits(std::string line){
    std::vector<int> row;
    for (char c : line) row.push_back((int) c - 48);
    return row;
}

std::vector<std::vector<int>> generateForest(std::string filename){
    std::fstream file;
    file.open(filename, std::ios_base::in);
    std::vector<std::vector<int>> forest;
    while (!file.eof()){
        //use of & reference
        std::string line = readLine(file);
        std::vector<int> row = toDigits(line);
        forest.push_back(row);
    }
    file.close();
    return forest;
}

void printForest(std::vector<std::vector<int>> forest){
    for (std::vector<int> row : forest){
        for (int tree : row) std::cout << tree;
        std::cout << std::endl;
    }
}

bool isVisible(std::vector<std::vector<int>> &forest, int i, int j){
//    std::cout << i <<  "  " << j << std::endl;
    int tree = forest[i][j];
    //check upwards
    bool visibleUpwards = true;
    for (int _i = i-1; _i >= 0; --_i){
        int otherTree = forest[_i][j];
        if (otherTree >= tree) {
            visibleUpwards = false;
            break;
        }
    }
    if (visibleUpwards) return true;
    //check leftwards
    bool visibleLeftwards = true;
    for (int _j = j-1; _j >= 0; --_j){
        int otherTree = forest[i][_j];
        if (otherTree >= tree) {
            visibleLeftwards = false;
            break;
        }
    }
    if (visibleLeftwards) return true;
    //check downwards
    bool visibleDownwards = true;
    for (int _i = i+1; _i < forest.size(); ++_i){
//        std::cout << forest.size() << std::endl;
        int otherTree = forest[_i][j];
        if (otherTree >= tree) {
            visibleDownwards = false;
            break;
        }
    }
    if (visibleDownwards) return true;

    //check rightwards
    bool visibleRightwards = true;
    for (int _j = j+1; _j < forest[i].size(); ++_j){
        int otherTree = forest[i][_j];
        if (otherTree >= tree) {
            visibleRightwards = false;
            break;
        }
    }
    if (visibleRightwards) return true;
    return visibleUpwards or visibleDownwards or visibleLeftwards or visibleRightwards;
}

int countVisible(std::vector<std::vector<int>> forest){
    int visibleCounter = 0;
    for (int i = 0; i < forest.size(); ++i){
        for (int j = 0; j < forest[i].size(); ++j) {
            if (isVisible(forest, i, j)) ++visibleCounter;
        }

    }
    return visibleCounter;
}
int scenicScore(std::vector<std::vector<int>> &forest, int i, int j){
    int tree = forest[i][j];
    //check upwards
    int scoreUpwards = 0;
    for (int _i = i-1; _i >= 0; --_i){
        ++scoreUpwards;
        int otherTree = forest[_i][j];
        if (otherTree >= tree) {
            break;
        }
    }
    //check downwards
    int scoreDownwards = 0;
    for (int _i = i+1; _i < forest.size(); ++_i){
        ++scoreDownwards;
        int otherTree = forest[_i][j];
        if (otherTree >= tree) {
            break;
        }
    }
    //check leftwards
    int scoreLeftwards = 0;
    for (int _j = j-1; _j >= 0; --_j){
        ++scoreLeftwards;
        int otherTree = forest[i][_j];
        if (otherTree >= tree) {
            break;
        }
    }
    //check rightwards
    int scoreRightwards = 0;
    for (int _j = j+1; _j < forest[i].size(); ++_j){
        ++scoreRightwards;
        int otherTree = forest[i][_j];
        if (otherTree >= tree) {
            break;
        }
    }
    return scoreUpwards*scoreDownwards*scoreLeftwards*scoreRightwards;
}
int findBestScenicScore(std::vector<std::vector<int>> &forest){
    std::vector<std::vector<int>> scoreForest(forest.size());
    for (int i = 0; i < forest.size(); ++i) {
//        printForest(scoreForest);
        for (int j = 0; j < forest[i].size(); ++j) scoreForest[i].push_back(scenicScore(forest, i, j));
    }
    int max = 0;
    for (std::vector<int> row : scoreForest) {
        int tempMax = *std::max_element(row.begin(), row.end());
        if (tempMax > max) max = tempMax;
    }
    return max;
}
int main() {
    std::vector<std::vector<int>> forest = generateForest("input.txt");
//    printForest(forest);
//    std::cout << countVisible(forest);
    std::cout << findBestScenicScore(forest);
    return 0;
}
