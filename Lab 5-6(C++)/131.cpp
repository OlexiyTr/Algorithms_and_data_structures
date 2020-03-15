#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main1() {
	string word;
	vector <int> arr(256), arr1;
	int n;
	for (int i = 0; i < arr.size(); i++) arr[i] = 0;
	cin >> word;
	for (int i = 0; i < word.size(); i++){
		arr[word[i] + 127]++;
	}
	cin >> n;
	int rez = 0;
	for (int i = 0; i < n; i++){
		cin >> word;
		arr1 = arr;
		bool words = true;
		for (int j = 0; j < word.size(); j++){
			arr1[word[j] + 127]--;
			if (arr1[word[j] + 127] < 0){
				words = false;
				break;
			}
		}
		rez += words;
	}
	cout << rez << endl;     
	return 0;
}