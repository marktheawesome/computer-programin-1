#include <iostream>
#include <ctime>
#include <chrono>
using namespace std;
using namespace std::chrono;

int million = 4000000;
int total = 0 ;
int a = 1;
int b = 1;

int main()
{

    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    while (a+b <= million)
    {
        int c = a + b;
        if (c % 2 == 0)
        {
            total = total + c;
        }
        b,a = c,b;
    }

    cout << total;
    cout << "\n";
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>( t2 - t1 ).count();

    cout << duration;
    cout << " microseconds";
    cout << "\n";
}