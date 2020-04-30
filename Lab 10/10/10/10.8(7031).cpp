#include <iostream>
#include <string.h>

#define MAX 100000

using namespace std;

int t, rev;	

void mycount(int *a, int xleft, int xright, int yleft, int yright)
{
	const int len = xright - xleft + 1;
	int curr = 0, q = 0, result[len];
	memcpy(result, a + xleft, len * sizeof(int));
	while (curr < len && yleft <= yright){
		while (result[q] <= a[yleft] + t && q < len)
			q++;
		if (result[curr] <= a[yleft])
			a[xleft++] = result[curr++];
		else 
			a[xleft++] = a[yleft++], rev += len - q;
	}
	while (curr < len)
		a[xleft++] = result[curr++];
}

void Cut(int *a, int left, int right)
{
	if (left >= right) {
		return;
	}
	int middle = (left + right) / 2;
	Cut(a, left, middle);
	Cut(a, middle + 1, right);
	mycount(a, left, middle, middle + 1, right);
}

int main() {
	int i, n, lst[MAX];
	cin >> n >> t;
	for (i = 0; i < n; i++) cin >> lst[i];
	Cut(lst, 0, n - 1);
	cout << rev << endl;
	system("pause");
	return 0;
}