#include <iostream>
using namespace std;

class Bank {
private:
  int amount;

public:
  Bank(int amount) { this->amount = amount; }

  void getBalance() { cout << "Balance is: " << amount << endl; }

  void deposit(int depositAmount) {
    if (depositAmount > 0) {
      this->amount = this->amount + depositAmount;
    } else {
      cout << "Invalid deposit amount!" << endl;
    }
  }

  void withdraw(int amount) {
    if (amount <= 0) {
      cout << "Invalid withdrawal amount!" << endl;
    } else if (amount <= this->amount) {
      this->amount = this->amount - amount;
    } else {
      cout << "Insufficient balance!" << endl;
    }
  }
};
int main() {
  Bank o(100);

  o.getBalance();

  o.deposit(17220);
  o.getBalance();

  o.withdraw(1560);
  o.getBalance();

  return 0;
}