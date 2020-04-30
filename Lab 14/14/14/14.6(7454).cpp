#include <iostream>

using namespace std;

class Node
{
public:
	int data;
	Node *next;
	Node() : next(NULL) {};
	Node(int data, Node *next = NULL) : data(data), next(next) {};
};

class List
{
public:
	Node *head, *tail;
	List() : head(NULL), tail(NULL) {};
	void addToTail(int val);
	int hasCycle(void);
};

int List::hasCycle(void) {
	Node *slow = head, *fast = head;
	while (slow && fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast) {
			return 1;
		}
	}
	return 0;
}

void List::addToTail(int val) {
	if (tail != NULL) {
		tail->next = new Node(val);
		tail = tail->next;
	}
	else
		head = tail = new Node(val);
}

int main(void) {
	List lst;
	int p, a, b, c, m, n;
	int i, val, k;
	scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &m, &n);
	lst.addToTail(p);
	for (i = 1; i < n; i++)
		lst.addToTail((a*lst.tail->data*lst.tail->data + b*lst.tail->data + c) % m);
	k = (a*lst.tail->data*lst.tail->data + b*lst.tail->data + c) % m;
	if (k < m / 2) {
		k = k % n - 1;
		Node* tmp = lst.head;
		i = 0;
		while (i <= k) {
			tmp = tmp->next;
			i++;
		}
		lst.tail->next = tmp;
	}
	cout << lst.hasCycle() << endl;
	system("pause");
	return 0;
}