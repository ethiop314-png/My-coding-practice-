#include <iostream>
#include <string>

using namespace std;

int main() {
    int amete_mihret, amete_alem, wenber, abeqte, metqe;
    
    cout << "እንኳን ወደ ባሕረ ሐሳብ ማስያ መጡ!" << endl;
    cout << "እባክዎ ዓመተ ምሕረቱን ያስገቡ (ለምሳሌ፦ 2016): ";
    cin >> amete_mihret;

    // 1. ዓመተ ዓለምን ማስላት (5500 ዓመተ ፍዳ ተደምሮ)
    amete_alem = amete_mihret + 5500;

    // 2. ወንበርን ማስላት (ለአውደ ቀመር 19 መድበል)
    // ዓመተ ዓለም ለ 19 ተካፍሎ ቀሪው ሲቀነስ 1
    wenber = (amete_alem % 19) - 1;
    
    // ወንበር ከዜሮ በታች ከሆነ 18 ይሆናል
    if (wenber < 0) {
        wenber = 18;
    }

    cout << "\n--- ውጤት ---" << endl;
    cout << "ዓመተ ዓለም: " << amete_alem << endl;
    cout << "ወንበር: " << wenber << endl;
    
    /* 
       ማስታወሻ፡ ከዚህ በኋላ አበቅቴን እና መጥቅዕን በማስላት 
       የነነዌ ጾም የሚውልበትን ቀን ማግኘት ይቻላል።
    */

    return 0;
}
