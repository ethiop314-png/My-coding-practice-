#include<iostream>
using namespace std;
void checknumber(int num){
if (num%2==0){
cout<< num<<" is an even number"<<endl;}
else{
cout<<num <<"is an odd number :"<<endl;}
}
int main(){
int number;
cout<<"Enter a number :";
cin>>number;
checknumber(number);
return 0;
}
