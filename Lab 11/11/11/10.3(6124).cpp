#include <iostream>
#include <string>
using namespace std;

struct node {
	int value = 0;
	node* next = NULL;
	node(int val, node* _next) : value(val), next(_next) {}
};

struct stack {
	int _size = 0;
	node* top = NULL;
public:
	void push(int n);
	bool empty();
	int pop();
	int back();
	int size();
	void clear();
};

void stack::push(int n) {
	top = new node(n, top);
	_size++;
}
bool stack::empty() {
	return _size == 0;
}
int stack::pop() {
	node* next = top->next;
	int topVal = top->value;
	delete top;
	top = next;
	_size--;
	return topVal;
}
int stack::back() {
	return top->value;
}
int stack::size() {
	return _size;
}
void stack::clear() {
	while (!empty()) pop();
}

int main() {
	string t;
	int val;
	stack s;
	while (cin >> t) {
		if (t == "push") {
			cin >> val;
			s.push(val);
			cout << "ok" << endl;
		}
		else if (t == "pop") {
			if (s.empty())
				cout << "error" << endl;
			else {
				val = s.pop();
				cout << val << endl;
			}
		}
		else if (t == "back") {
			if (s.empty())
				cout << "error" << endl;
			else
				cout << s.back() << endl;
		}
		else if (t == "size") cout << s.size() << endl;
		else if (t == "clear") {
			s.clear();
			cout << "ok" << endl;
		}
		else if (t == "exit") {
			cout << "bye" << endl;
			break;
		}
	}
	return 0;
}