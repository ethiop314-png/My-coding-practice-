#include<iostream>
using namespace std;
int main()
{int mark;
char grade;
cout<<"Enter your mark"<<endl;
cin>>mark;
switch(mark/10) 
{
	case 9:
	grade='A';
	break;
	case 8:
	grade='B';
	break;
	case 7:
	grade='C';
	break;
	case 6:
	grade='D';
	break;
	default:
	grade='F';}
	cout<<"your grade is :"<<grade;
	return 0;           
}
                 
