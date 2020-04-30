#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Stack {
public:
	Stack(int size);
	void push(int x);
	void pop();
	int getMin();
private:
	int* m;
	int size;
};

Stack::Stack(int size = 1000001) {
	m = new int[size];
	this->size = 0;
}

void Stack::push(int x) {
	if (size == 0)
		m[size++] = x;
	else{
		int pos = size - 1;
		m[size++] = min(x, m[pos]);
	}
}

void Stack::pop() {size--;}

int Stack::getMin() {return m[size - 1];}

int main(void) {
	Stack s;
	int n, st, x;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &st);
		if (st == 1){
			scanf("%d", &x);
			s.push(x);
		}
		else if (st == 2)
			s.pop();
		else
			printf("%d\n", s.getMin());
	}
	system("pause");
	return 0;
}