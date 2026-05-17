/* password attempts
Stream Library*/
#include<iostream>
using namespace std;
int main() {
string name;
cout<<"what is your name\n"<<endl;
cin>>name;
cout<<"I am "<< name<<endl;
   string secret_pass="E$t2^H+p";
  int attempts;
for (attempts=3;attempts>0;){
     string user_input;
     cout << "Enter password: ";
     cin>>user_input;
if(user_input==secret_pass){
  cout<< name <<" .wellcome\n"<<endl;
  break;
  }
else{
   attempts-=1;
   cout<<name <<" .you enter incorrect password.please try agian\n"<<endl;
}
{if (attempts==0)
     cout<<name <<" .your password locked for 24 hours\n"<<endl;
}}
    return 0;
return 0;
}/* Yihun 
     shambel */
