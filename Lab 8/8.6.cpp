#include <iostream>
#include <iterator>
#include <utility> 
#include <vector>

using namespace std;
#define maxn 100000

vector <pair <int, int> > a;
int n;

void merge(int lefthalf, int righthalf) {
	if (righthalf == lefthalf)
		return;
	if (righthalf - lefthalf == 1) {
		if (a[righthalf].first < a[lefthalf].first)
			swap(a[righthalf], a[lefthalf]);
		return;
	}
	int mid = lefthalf + (righthalf - lefthalf) / 2;
	merge(lefthalf, mid);
	merge(mid + 1, righthalf);
	vector <pair <int, int> > buf;
	buf.resize(righthalf- lefthalf+1);
	int xl = lefthalf;
	int xr = mid + 1;
	int cur = 0;
	while (righthalf - lefthalf + 1 != cur) {
		if (xl > mid)
			buf[cur++] = a[xr++];
		else if (xr > righthalf)
			buf[cur++] = a[xl++];
		else if (a[xl].first > a[xr].first)
			buf[cur++] = a[xr++];
		else buf[cur++] = a[xl++];

	}
	for (int i = 0; i < cur; i++)
		a[i + lefthalf] = buf[i];
}

int main() {
	cin >> n;
	int k, l;
	a.resize(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i].first >> a[i].second;
	}

	merge(0, n - 1);
	for (int i = 0; i < n; i++)
		cout << a[i].first << " " << a[i].second << endl;
	system("pause");
	return 0;
}