#include<iostream>
class Box {
    int len,bre,hei;
    public:
    void setData(int l, int b, int h) {
        len = l;
        bre = b;
        hei = h;
    }
    void setData(){
        len = 3;
        bre = 6;
        hei = 5;
    }
    void volume() {
        std::cout << "Volume is: " << len*bre*hei << std::endl;
    }
};
int main() {
    Box b1;
    b1.setData(2, 4, 6);
    b1.volume();

    Box b2;
    b2.setData();
    b2.volume();

    return 0;
}