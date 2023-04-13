#include <iostream>
using namespace std;

void Menu() {
	cout << "\tMENU\n";
	cout << "1. Check Balance \n";
	cout << "2. Withdraw Cash \n";
	cout << "3. Send Money \n";
	cout << "4. Reset/ Change Pin \n";
	cout << "5. Exit \n";
}

int main() {
	
	int option;
	double amount, balance = 1000;
	string pin1, pin = "0000", reciever;
	
	do {
		Menu();
		cout << "\n Option: ";
		cin >> option;
		system("cls");
		
		switch (option) {
			
			case 1: cout << "Balance is: $" << balance << "\n\n";				
				break;
				
			case 2: cout << "Withdraw amount: $";
				cin >> amount;
				if (amount <= balance) {
					balance -= amount;
				}
				else
					cout << "Not Enough Balance.\n\n";
				break;
				
			case 3: cout << "Amount to send: $";
				cin >> amount;
				if (amount <= balance) {
					cout << "Reciever's address: ";
					cin >> reciever;
					cout << "Enter Pin: ";
					cin >> pin1;
					system("cls");
					if (pin1 == pin){
						balance -= amount;
						cout << "$" << amount << " Successfully sent.\n\n";
					}
					else
						cout << "Incorrect Pin.\n";
				}
				else
					cout << "Not Enough Balance.\n\n";				
				break;
				
			case 4: for (int i = 0; i < 3; i++) {
				cout << "Enter Current Pin: ";
				cin >> pin1;
				if (pin1 == pin) {
					cout << "Set/ Enter New Pin: ";
					cin >> pin1;
					if (pin1.size() == 4){
						pin = pin1;
						i += 3;
					}
					else
						cout << "Pin must be 4 numbers.\n";
				}
			}
			system("cls");
			cout << "Account have been disabled for the next 24 hours.\n";
			option = 5;	
				break;
		}	
	} while (option != 5);
	
	system("pause>0");
}
