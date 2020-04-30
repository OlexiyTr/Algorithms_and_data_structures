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
	void Print(void);
	void PrintReverse(void);

	void H_1(Node *node);
	void H_2(Node *node);
};
/*
void List::addToTail(int val) {
	if (tail != NULL) {
		tail->next = new Node(val);
		tail = tail->next;
	}
	else 
		head = tail = new Node(val);
}

void List::H_1(Node *node){
	if (node == NULL) 
		return;
	printf("%d ", node->data);
	H_1(node->next);
}*/

void List::H_2(Node *node){
	if (node == NULL) 
		return;
	H_2(node->next);
	printf("%d ", node->data);
}
/*
void List::Print(void) {
	H_1(this->head);
	printf("\n");
}*/

void List::PrintReverse(void){
	H_2(this->head);
	printf("\n");
}

int main1(void) {
	List lst;
	int i, n, val;
	scanf("%d", &n);
	for (i = 0; i < n; i++){
		scanf("%d", &val);
		lst.addToTail(val);
	}
	lst.Print();
	lst.PrintReverse();
	system("pause");
	return 0;
}