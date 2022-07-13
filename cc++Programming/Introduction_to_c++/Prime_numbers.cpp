#include <iostream>
using namespace std;
int main()
{
    int i , n ,flag = 0;
    cout<<"Enter the value of n ";
    cin>>n;
    for(i = 0 ; i = n/2 ; i++){
        if(n%i==0  ){
            cout<<"Number is not prime";
    
            flag = 1;
            break;
        }
    }
    if(flag==0){
        cout<<"NUmber is  Prime";
    }
}