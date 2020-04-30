#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

class Stack {
	int* m;
	int _size;
public:
	Stack(int _size);
	~Stack();
	void push(int v);
	int pop();
	int back();
	int size();
	void clear();
	void exit();
};

Stack::Stack(int _size = 110) {
	m = new int[_size];
	this->_size = 0;
}

Stack::~Stack() {
	delete[] m;
}

void Stack::push(int v) {
	m[_size++] = v;
	puts("ok");
}

int Stack::pop() {
	return m[--_size];
}

int Stack::back() {
	return m[_size - 1];
}

int Stack::size() {
	return _size;
}

void Stack::clear() {
	_size = 0;
	puts("ok");
}

void Stack::exit() {
	puts("bye");
}

int main(void) {
	int n;
	char str[100];
	Stack s;
	while (scanf("%s", &str)){
		if (strcmp(str, "push") == 0){
			scanf("%d", &n);
			s.push(n);
		}
		else if (strcmp(str, "pop") == 0){
			printf("%d\n", s.pop());
		}
		else if (strcmp(str, "back") == 0){
			printf("%d\n", s.back());
		}
		else if (strcmp(str, "size") == 0){
			printf("%d\n", s.size());
		}
		else if (strcmp(str, "clear") == 0){
			s.clear();
		}
		else {
			s.exit();
			break;
		}
	}
	system("pause");
	return 0;
}