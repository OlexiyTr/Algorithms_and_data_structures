#include <math.h>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

#define MAX 5000000

using namespace std;

struct node
{
	long long summa, add;
} items[4 * MAX];

void Push(int v, int LeftPos, int Middle, int RightPos)
{
	if (items[v].add)
	{
		items[2 * v].add += items[v].add;
		items[2 * v].summa += (Middle - LeftPos + 1) * items[v].add;
		items[2 * v + 1].add += items[v].add;
		items[2 * v + 1].summa += (RightPos - Middle) * items[v].add;
		items[v].add = 0;
	}
}

void Add(int v, int LeftPos, int RightPos, int L, int R, int Value)
{
	if (L > R) return;
	if ((LeftPos == L) && (RightPos == R)){
		items[v].add += Value;
		items[v].summa += (R - L + 1) * Value;
		return;
	}
	int Middle = (LeftPos + RightPos) / 2;
	Push(v, LeftPos, Middle, RightPos);
	Add(2 * v, LeftPos, Middle, L, min(Middle, R), Value);
	Add(2 * v + 1, Middle + 1, RightPos, max(L, Middle + 1), R, Value);
	items[v].summa = items[2 * v].summa + items[2 * v + 1].summa;
}

long long Get(int v, int LeftPos, int RightPos, int L, int R)
{
	if (L > R) return 0;
	if ((LeftPos == L) && (RightPos == R)) 
		return items[v].summa;
	int Middle = (LeftPos + RightPos) / 2;
	Push(v, LeftPos, Middle, RightPos);
	return Get(2 * v, LeftPos, Middle, L, min(Middle, R)) +
		Get(2 * v + 1, Middle + 1, RightPos, max(L, Middle + 1), R);
}
int main(void) {
	int i, q, L, R, p, Lnew, Rnew;
	scanf("%d %d %d %d", &q, &L, &R, &p);
	vector<int> arr(256,0);
	for (i = 0; i < q; i++) {
		Add(1, 0, 255, L, R, 1);
		L = Get(1, 0, 255, L, R) % p;
		R = 255 - L;
	}
	printf("%d", Get(1, 0, 255, 0, 255));
	system("pause");
	return 0;
}