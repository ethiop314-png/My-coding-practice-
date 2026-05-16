#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int total[3][3];
    int p[3][3];
    int q[3][3];

    // Input first matrix
    cout << "Enter the first matrix (3x3):" << endl;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> p[i][j];
        }
    }

    // Input second matrix
    cout << "Enter the second matrix (3x3):" << endl;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> q[i][j];
        }
    }

    // Add matrices and display result
    cout << "Sum of the matrices:" << endl;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            total[i][j] = p[i][j] + q[i][j];
            cout << setw(4) << total[i][j];
        }

        cout << endl;
    }

    return 0;
}
