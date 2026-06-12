#include<iostream>
using namespace std;

class parent {
    public:
    void display() {
        cout << "Hello from parent class." << endl;
    }
};
class child : public parent {
    public:
    void display() {
        cout << "Hello from child class." << endl;
    }
};
int main() {
    parent *p;
    child c;
    p = &c;
    p->display();
    return 0;
}