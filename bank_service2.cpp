#include <iostream>
using namespace std;

int main() {
    string name;
    string account;
    string service;
    int balance = 100;
    int deposit, withdraw;
    cout << "Welcome our customer" << endl;
    while (true) {
        cout << "What service do you want? deposit or withdraw" << endl;
        cin >> service;

        if (service == "deposit" || service == "withdraw") {
            break; 
        }
        cout << "Invalid service! Please enter deposit or withdraw." << endl;
    }
    cout << "What is your name?" << endl;
    cin >> name;
    while (true) {
        cout << "Enter your 8-digit account number" << endl;
        cin >> account;

        if (account.length() == 8) {
            break;
        }

        cout << name
             << ", invalid account number! Please enter exactly 8 digits."
             << endl;
    }
    if (service == "deposit") {
        cout << name
             << ", how many dollars do you want to deposit?" << endl;
        cin >> deposit;

        balance = balance + deposit;

        cout << name
             << ", your new balance: $"
             << balance << endl;
    }
    else if (service == "withdraw") {
        cout << name
             << ", how much money do you want to withdraw?" << endl;
        cin >> withdraw;
if (withdraw > balance) {
            cout << name
                 << ", you don't have enough money to withdraw" << endl;
        }
        else {
            balance = balance - withdraw;
 cout << name
                 << ", wait, your withdrawal is in process" << endl;
cout << name
                 << ", withdrawal amount: $"
                 << withdraw << endl;
                        cout << name
                 << ", remaining balance: $"
                 << balance << endl;
        }
    }
  return 0;
}	
