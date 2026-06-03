#include <iostream>
using namespace std;

class Bank
{
private:
    int amount;

public:
    Bank(int amount)
    {
        this->amount = amount;
    }

    void getBalance()
    {
        cout << "Balance is: " << amount << endl;
    }

    void deposit(int amount)
    {
        this->amount += amount;
    }

    void withdraw(int amount)
    {
        if (amount > this->amount)
        {
            cout << "Insufficient balance!" << endl;
        }
        else
        {
            this->amount = this->amount - amount;
        }
    }
};
int main()
{
    Bank o(1000);

    o.getBalance();

    o.deposit(12220);
    o.getBalance();

    o.withdraw(2000);
    o.getBalance();

    return 0;
}