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
	void AddToTail(int val);
	void RotateRight(int k);
	void Print(void);

	void H_1(Node *node);
};

void List::RotateRight(int k) {
	if (!head)
		return;
	Node* node = head;
	int len = 1;
	while (node->next != NULL) {
		node = node->next;
		len++;
	}
	if (k > len)
		k %= len;
	k = len - k;
	if (k == 0)
		return;
	Node* curr = head;
	int counter = 1;
	while (counter < k && curr != NULL) {
		curr = curr->next;
		counter++;
	}
	if (curr == NULL)
		return;
	Node* knode = curr;
	node->next = head;
	head = knode->next;
	knode->next = NULL;
}
/*
void List::AddToTail(int val) {
	if (tail != NULL) {
		tail->next = new Node(val);
		tail = tail->next;
	}
	else
		head = tail = new Node(val);
}

void List::H_1(Node *node) {
	if (node == NULL)
		return;
	printf("%d ", node->data);
	H_1(node->next);
}


void List::Print(void) {
	H_1(this->head);
	printf("\n");
}
*/

int main2(void) {
	List lst;
	int i, n, val, k;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &val);
		lst.AddToTail(val);
	}
	while (scanf("%d", &k) == 1)
	{
		lst.RotateRight(k);
		lst.Print();
	}
	system("pause");
	return 0;
}