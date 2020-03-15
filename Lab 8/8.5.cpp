#include <iostream>
#include <string> 

using namespace std;

#define LEN 20000

int main(void){
	int i, n, a, b, counter;
	int arr[LEN];

	while (scanf("%d", &n) == 1)
	{
		for (i = 0; i < n; i++) scanf("%d", &arr[i]);
		scanf("%d %d", &a, &b);
		counter = 0;
		for (i = 0; i < n; i++) {
			if ((arr[i] >= a) && (arr[i] <= b)) counter++;
		}
		printf("%d\n", counter);
	}
	system("pause");
	return 0;
}