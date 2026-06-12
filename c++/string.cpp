#include<iostream>
using namespace std;
int main()
{
    string a;
    char str[]="Indus";
    cout<<"\n"<<str;
    for(int i=0;str[i]!='\0';i++)
    {
        cout<<"\n"<<str[i];
    }
    cin>>a;
    cout<<"\n"<<a;
    char ch;
    cin>>ch;
    if( ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
    {
        cout<<"\nVowel";
    }
    else
    {
        cout<<"\nConsonant";
    }


    return 0;
    
}