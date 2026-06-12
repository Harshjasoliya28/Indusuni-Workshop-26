#include<iostream>


class abc{
    public:
    int a;
    abc operator * (abc obj){
        abc temp;
         temp.a = a * obj.a;
        return temp;
    }
};
int main() {
    abc obj1, obj2, obj3;
    obj1.a = 5;
    obj2.a = 10;

    obj3 = obj1 * obj2;
    std::cout << obj3.a;

    return 0;
}