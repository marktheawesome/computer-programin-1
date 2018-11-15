#include <iostream>
using namespace std;

int low = 1;
int high = 20;
int limit = 5;


void start_screen ()
{
    cout <<R"(
    ***********************************
    ******    Guess A Number!    ******
    ***********************************
    )";
    cin ;
}


void end_screen ()
{
    cout <<R"(
    Bye.
    This awesome game was made by Mark Gyomory
    )";
}

int play_again()
{
    while(1)
    {
        cout<<("would you like to play again?(y/n)");
        char again;
        cin >> again;

        if(again == 'y')
            return 1;

        else if(again == 'n')
            return 0;
            
        else;
            cout<<("Invalid input. Please enter y or n.");
    }
    

};

int pick_number(int low, int high)
{
 
    cout<<("I'm thinking of a num from " + to_string( low )  + " to " + to_string( high )  + ".");
    return (rand()%20)+1;
}

// int pick_range()
// {
//     int low = rand() % 100 + 1;
//     int high = rand() % 100 + 1;

//     if (low > high)
//         low, high = high, low;
//     cout <<("I'm thinking of a number from " + low + ' to ' + high + '.');
//     return (low, high);
// };

int get_guess()
{
    while (1)
    {
        cout<<("");
        cout<<("Take a guess:");
        int num;
        cin>>num;
        return num;
    };
};

int check_guess(int rand, int guess)
{
    if (guess > rand)
        cout<<("You guessed too high.");

    else if (guess < rand)
        cout<<("You guessed too low.");

    else if (guess == rand)
        return 1;

    else
        return 0;
    return 0;
};


void show_result(int got_it)
{
    if (got_it == 1)
        cout<< ("You got it. ");
    else
        cout<<("You are such a LOSER!!!!!!!!!");
};

void play()
{
    int rand = pick_number(low,high);
    int got_it = 0;
    int tries = 0;

    while(got_it == 0 && tries < limit)
    {
        int guess = get_guess();
        got_it = check_guess(rand, guess);
        ++ tries;

    }
    show_result(got_it);
};


int main() 
{
    //cout << "Hello World!";
    start_screen ();
    int playing = 1;

    while (playing != 0)
    {
         play();
         int playing = play_again();
         return playing;
    };

    end_screen();

    return 0;
}


