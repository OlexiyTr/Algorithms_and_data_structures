#include <math.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

#define MAX 1000001
#define INF 2000000000
long long items[4 * MAX];
int m[MAX];

using namespace std;

void BuildTree(int *a, int v, int L, int R){
	if (L == R) items[v] = a[L];
	else{
		int Middle = (L + R) / 2;
		BuildTree(a, v * 2, L, Middle);
		BuildTree(a, v * 2 + 1, Middle + 1, R);
		items[v] = items[v * 2] + items[v * 2 + 1];
	}
}

/*
Якщо викон умова LeftPos == RightPos, це означає, що ми розглядаємо відрізок довжини 1.
Тоді повертаємо 1 якщо людина потрапляє до шару.
Якщо відрізо більше, то знаходимо індекс єлемента по середині. Тоді якщо сума людей зліва більше вантажопідйомності, то
нікого з правого піддерева вже не влізе і тоду ми шукаємо у лівому піддереві. 
В іншому випадку ми саджаємо всіх людей лівого піддерева до шару (Middle - LeftPos + 1) і шукаємо скільки людей влізе до шару правої частини.
В такому випадку потрібно від загальної ваги відняти вагу людей з лівого піддерева, що влізли до шару (max_w - items[v * 2])*/
int Get(int v, int LeftPos, int RightPos, int max_w) {
	if (LeftPos == RightPos) return items[v] <= max_w;
	int Middle = (LeftPos + RightPos) / 2;
	if (items[v * 2] > max_w)
		return Get(v * 2, LeftPos, Middle, max_w);
	else
		return Middle - LeftPos + 1 + Get(v * 2 + 1, Middle + 1, RightPos, max_w - items[v * 2]);
}

void update(int v, int LeftPos, int RightPos, int Position, int NewValue){
	if (LeftPos == RightPos) items[v] = NewValue;
	else
	{
		int Middle = (LeftPos + RightPos) / 2;
		if (Position <= Middle)
			update(v * 2, LeftPos, Middle, Position, NewValue);
		else update(v * 2 + 1, Middle + 1, RightPos, Position, NewValue);
		items[v] = items[v * 2] + items[v * 2 + 1];
	}
}
int main(void) {
	int i, n, k, x, y, q, op, Weight;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) scanf("%d", &m[i]);
	//SegmentTree tree = SegmentTree(arr);
	BuildTree(m, 1, 1, n);
	scanf("%d", &q);
	for (i = 0; i < q; i++){
		scanf("%d", &op);
		if (op == 1){
			scanf("%d", &Weight);
			printf("%d\n", Get(1, 1, n, Weight));
		}
		else{
			scanf("%d %d", &x, &y);
			update(1, 1, n, x, y);
		}
	}
	system("pause");
	return 0;
}