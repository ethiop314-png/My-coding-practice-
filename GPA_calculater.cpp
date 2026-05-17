#include<iostream>
using namespace std;
int main ()
{   float GPA1;
	float M,E,P,G,S,C,T;
	float sum;
	float GPA2;
	float GPA;
	float N;
	cout<<"Enter the  value"<<endl;
	cout<<"maths :";
	cin>>M;
	cout<<"English :";
	cin>>E;
	cout<<"psychology :";
	cin>>S;
	cout<<"geography :";
	cin>>G;
	cout<<"programming :";
	cin>>P;
	cout<<"civics :";
	cin>>C;
	cout<<"global trend :";
	cin>>T;
	sum=5*M+5*E+5*P+5*G+5*S+4*C+4*T;
	cout<<"sum ="<<sum<<endl;
	GPA2=sum/33;
	cout<<"second semister GPA :"<<GPA2<<endl;
	cout<<"first semister GPA :";
	cin>>GPA1;
	double entrance_score;
	cout<<"enter your entrance mark :";
	cin>>entrance_score;
	GPA=(GPA1+GPA2)/2;
	cout<<"GpA ="<<GPA<<endl;
	 N=(GPA*20)+(entrance_score*2)/60;
	cout<<"your mark is "<<N<<endl;
	return 0;
}
