#include <iostream>
#include <ctime>
using namespace std;

int start_s=clock();

int main()
{
    int CurrentNumber = 1;
    int toal = 0;
    int UpperNumber = 1000;
    int total = 0;

    
    for (1;CurrentNumber < UpperNumber;CurrentNumber++)
    {
        if (CurrentNumber % 3 == 0  || CurrentNumber % 5 == 0)
        {
             total = total + CurrentNumber;
        }
    }
    
    
    cout << to_string(total);
    cout << "\n";
    int stop_s=clock();
    cout << "time in milliseconds: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000  << endl;

    return 0;
};

