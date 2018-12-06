#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;



int pythagorean_triple(int a, int b, int c)
{
    c = c*c;
    if(c == ((a*a)+ (b*b)))
    {
        return 1;
    }
    else
    {
        return 0 ;
    }
}

int main()
{
    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    int i = 1000;
    int a =1;
    int b =1;
    int c =1;
    while (a < i/3)
    {
        b = 1;
        while(b < i/2)
        {
            c = i-(a+b);
            if(a + b + c == i && pythagorean_triple(a,b,c))
            {
                break;
            }
            b++;
        }
        if(a + b + c == i && pythagorean_triple(a,b,c))
            {
                break;
            }
        a++;
    }
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    int d = int(a)*int(b)*int(c);
    cout<<a;
    cout<<"\n";
    cout<<b;
    cout<<"\n";
    cout<<c;
    cout<<"\n";
    cout<<int(d) ;
    cout<<"\n";
    auto duration = duration_cast<microseconds>( t2 - t1 ).count();

    cout << duration;
    cout << " microseconds";
    cout << "\n";
    
}