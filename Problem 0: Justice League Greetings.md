
#include <iostream>
using namespace std;

int main() 
{   // the input from the user 
    string name ;
    getline(std::cin, name );
    
    // check constraints
    if (name.length() > 1 && name.length() <= 100) {
    
        cout << "Hello, "<< name <<"!"<< endl;
    }
    else {
        cout << "invalid; ";
    }

    return 0;
}
