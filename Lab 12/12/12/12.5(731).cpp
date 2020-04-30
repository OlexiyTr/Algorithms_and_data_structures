#include <string>
#include <iostream> 
#include <stack> 
#include <utility>
using namespace std;

bool isOperator(char x) {
	switch (x) {
	case '+':
	case '-':
	case '/':
	case '*':
		return true;
	}
	return false;
}

bool isOp(char x) {
	switch (x) {
	case '/':
	case '*':
		return true;
	}
	return false;
}

string preToInfix(string str) {
	stack<pair<string, char>> s;
	int len = str.size();
	for (int i = len - 1; i >= 0; i--) {
		if (isOperator(str[i])) {
			pair<string, char> op1 = s.top();
			s.pop();
			pair<string, char> op2 = s.top();
			s.pop();
			string temp;
			if (isOp(str[i])) {
				if ((op1.second == '+' || op1.second == '-'))
					op1.first = "(" + op1.first + ")";
				if ((op2.second == '+' || op2.second == '-'))
					op2.first = "(" + op2.first + ")";
			}
			if (str[i] == '-')
				if (op2.second == '+' || op2.second == '-')
					op2.first = "(" + op2.first + ")";
			if (str[i] == '/')
				if (op2.second == '*' || op2.second == '/')
					op2.first = "(" + op2.first + ")";
			if (str[i] == '*')
				if (op1.second == '/')
					op1.first = "(" + op1.first + ")";
			temp = op1.first + str[i] + op2.first;
			
			s.push(make_pair(temp,str[i]));
		}
		else {
			s.push(make_pair(string(1, str[i]), ' '));
		}
	}
	return s.top().first;
}

int main2() {
	string str;
	cin >> str;
	cout << preToInfix(str);
	system("pause");
	return 0;
}