#include <iostream>
using namespace std;

int main() {
    string name;
    int account;
    int withdraw, deposit;
    int balance = 100;

    cout << "Welcome our customer" << endl;
    cout << "What service do you want? deposit or withdraw" << endl;

    string service;
    cin >> service;

    cout << "What is your name?" << endl;
    cin >> name;

    cout << "Enter " << name << " your account number" << endl;
    cin >> account;

    if (service == "deposit") {
        cout << name << ", how many birr do you want to deposit?" << endl;
        cin >> deposit;

        balance = balance + deposit;

        cout << name << ", your balance: " << balance << " birr" << endl;
    }

    else if (service == "withdraw") {
        cout << name << ", how much money do you want to withdraw?" << endl;
        cin >> withdraw;

        if (withdraw > balance) {
            cout << name << ", you don't have enough money to withdraw" << endl;
        } 
        else {
            balance = balance - withdraw;

            cout << name << ", wait, your withdrawal is in process" << endl;
            cout << name << ", your withdrawal amount: " << withdraw << " birr" << endl;
            cout << name << ", your remaining balance: " << balance << " birr" << endl;
        }
    }
    else {
        cout << name << ", you entered an invalid service" << endl;
    }

    return 0;

