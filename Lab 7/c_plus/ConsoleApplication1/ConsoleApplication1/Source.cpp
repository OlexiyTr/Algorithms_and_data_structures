#include <iostream>
#include <string> 

using namespace std;

#define MAX_LEN 0x7ffffff

unsigned long long w(unsigned long long x) {
	unsigned long long s = 0;
	while (x != 0) {
		s = s + x % 10;
		x = x / 10;
	}
	return s;
}

bool comp(unsigned long long x, unsigned long long y) {
	if (w(x) > w(y)) return true;
	if (w(x) == w(y) && to_string(x) > to_string(y)) return true;
	return false;
}

void Sort(unsigned long long* arr, unsigned long long n) {
	unsigned long long counter = 0;
	for (unsigned long long i = 1;i<n;i++) {
		for (unsigned long long j = i; j>0;j--) {
			if (comp(arr[j - 1], arr[j])) {
				counter++;
				unsigned long long tmp = arr[j - 1];
				arr[j - 1] = arr[j];
				arr[j] = tmp;
			}
		}
	}
}

int main() {
	unsigned long long n;
	cin >> n;
	unsigned long long k;
	cin >> k;
	unsigned long long* a = new unsigned long long[MAX_LEN];
	for (unsigned long long i = 0; i < n+1; i++) {
		a[i] = i;
	}
	Sort(a, n+1);
	unsigned long long l = 0;
	while (l < n+1)
	{
		if (a[l] == k) {
			break;
		}
		l++;
	}
	cout << l << endl;
	cout << a[k] << endl;
	system("pause");
	delete a;
	return 0;
}
