#include <iostream>
using namespace std;

class AreaCalculator {
public:

    // Function to calculate area of circle
    double area(double radius) {
        return 3.14159 * radius * radius;
    }

    // Function to calculate area of rectangle
    double area(double length, double width) {
        return length * width;
    }

    // Function to calculate area of square
    int area(int side) {
        return side * side;
    }
};

int main() {
    AreaCalculator calc;

    double radius, length, width;
    int side;

    cout << "Enter radius of circle: ";
    cin >> radius;
    cout << "Area of Circle = " << calc.area(radius) << endl;

    cout << "\nEnter length and width of rectangle: ";
    cin >> length >> width;
    cout << "Area of Rectangle = " << calc.area(length, width) << endl;

    cout << "\nEnter side of square: ";
    cin >> side;
    cout << "Area of Square = " << calc.area(side) << endl;

    return 0;
}
