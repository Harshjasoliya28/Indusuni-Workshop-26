#include<iostream>
#include<string>
using namespace std;

class student {
    public:
    float a;
 
    void square(float lenght){
        a = lenght * lenght;
     
     }
};
  
int main() {
    student s1; 
    s1.square(5);
        cout<<s1.a<<endl;
    
        return 0;
}