#include <iostream>
#include <ctime>
using namespace std;

int start_s=clock();;
int million = 4000000;
int total = 0 ;
int a = 1;
int b = 1;

int main()
{

    while (a+b <= million)
    {
        int c = a + b;
        if (c % 2 == 0)
        {
            total = total + c;
        }
        b,a = c,b;
    }

    int stop_s=clock();
    cout << "time in milliseconds: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000  << endl;
    cout << total;
    cout << "\n";
}