#include <iostream>
#include <string>
#include <stdlib.h>
#include <string.h>

using namespace std;

long long max_num = 0;
long long numbers[100000];

long long multiplyList(long long* numbers, int n) {
	long long result = 1;
	for (int i = 0; i < n;i++)
		result = result * numbers[i];
	return result;
}

void funk(char* arr, int m, int n, long long* numbers) {
	if (m == 1) {
		numbers[n - m] = atoll(arr);
		long long new_max = multiplyList(numbers, n);
		if (new_max > max_num)
			max_num = new_max;
		return;
	}
	size_t len = strlen(arr) - m + 2;
	for (int pos = 1; pos < len; pos++) {
		char str1[40];
		strncpy(str1, arr, pos);
		str1[pos] = '\0';
		numbers[n - m] = atoll(str1);
		funk(arr + pos, m - 1, n, numbers);
	}
}

int main1(void) {
	char num[80];
	int m;
	while (scanf("%s",num) == 1)
	{
		scanf("%d", &m);
		if (strlen(num) == 0)
			break;
		max_num = 0;
		funk(num, m, m, numbers);
		cout << max_num << endl;
	}
	system("pause");
	return 0;
}