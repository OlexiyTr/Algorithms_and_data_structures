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
	void Print(void);
	void reverse(Node** head);
	void ReorderList();

	void H_1(Node *node);
};

void List::reverse(Node** head)
{
	Node *prev = NULL, *curr = *head, *next;
	while (curr) {
		next = curr->next, curr->next = prev;

		prev = curr, curr = next;
	}
	*head = prev;
}

void List::ReorderList()
{
	//знаходимо середину
	Node *slow = head, *fast = slow->next;
	while (fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;
	}

	Node* head1 = head, *head2 = slow->next;
	slow->next = NULL;

	reverse(&head2);
	head = new Node(0);

	Node* curr = head;
	while (head1 || head2) {
		if (head1) {
			curr->next = head1;
			curr = curr->next;
			head1 = head1->next;
		}
		if (head2) {
			curr->next = head2;
			curr = curr->next;
			head2 = head2->next;
		}
	}

	head = head->next;
}

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

int main5(void) {
	List lst;
	int i, n, val, k;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &val);
		lst.AddToTail(val);
	}
	lst.ReorderList();
	lst.Print();
	system("pause");
	return 0;
}