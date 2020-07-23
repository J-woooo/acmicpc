#include <iostream>
using namespace std;

int main(void)
{
	int n, i;
	cin >> n;
	int *arr = new int[n];
	for (i = 0; i < n; i++) {
		int a, b;
		cin >> a >> b;
		arr[i] = a + b;
	}
	for (i = 0; i < n; i++)
		cout << arr[i] << endl;
}
