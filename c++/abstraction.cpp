#include<iostream>
using namespace std;
class ATM{
    private:
    int balance=10000;
    public:
    ATM(int balance){
        this->balance = balance;
    }
    
    void withdraw(int amount){
        if(amount <= balance){
            
        this->balance = this->balance - amount;
    }else{
        cout << "Insufficient balance." << endl;
    }
    }
};
int main(){
    ATM o(10000);
    
    o.withdraw(2000);
   
    return 0;
}