#include <iostream>
#include <bits/stdc++.h>
#include <math.h>
using namespace std;
#define ITERS 75

map<unsigned long long int, map<unsigned long long int, unsigned long long int> > dp;

unsigned long long int count_digits(unsigned long long int number){
    if (number == 0)
        return 0;
    return 1 + count_digits(number / 10);
}

unsigned long long int calculate(unsigned long long int num, int index){

    if( dp[index][num] != 0)
        return dp[index][num];

    if( index == ITERS ){
        return 1;
    }

    if( num == 0 ){
        unsigned long long int result = calculate(1, index + 1);
        dp[index][num] = result;
        return result;
    }
    unsigned long long int size = count_digits(num);
    if (size % 2 == 0){
        unsigned long long int half1 = num / (pow(10,(size / 2)));
        unsigned long long int half2 = num % static_cast<unsigned long long int>(pow(10, (size / 2)));
        unsigned long long int result = calculate(half1, index + 1) + calculate(half2, index + 1);
        dp[index][num] = result;
        return result;
    }

    unsigned long long int result = calculate(num * 2024, index + 1);
    dp[index][num] = result;
    return result;
}

int main(){
    // unsigned long long int input[] = {125, 17};
    unsigned long long int input[] = {92, 0, 286041, 8034, 34394, 795, 8, 2051489};
    unsigned long long int total = 0;

    // Init map
    for (unsigned long long int i = 0; i < ITERS + 2; ++i) {
        dp[i] = map<unsigned long long int, unsigned long long int>();
    }

    for (int i = 0; i < (sizeof(input) / sizeof(*input)); i++){
        total += calculate(input[i], 0);
    }

    cout << total << endl;

    return 0;
}