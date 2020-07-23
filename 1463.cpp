#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

class One {
private:
	int n;
	int* arr = new int[1000001];
public:
	void setNum() {
		cin >> n;
		memset(arr, 0, sizeof(int) * (n + 1));
	}

	void solution() {
		arr[1] = 0;
		for (int i = 2; i <= n; i++) {
			arr[i] = arr[i - 1] + 1;
			if (i % 2 == 0) {
				arr[i] = min(arr[i], arr[i / 2] + 1);
			}
			if (i % 3 == 0) {
				arr[i] = min(arr[i], arr[i / 3] + 1);
			}
		}
	}
	void printNum() {
		cout << arr[n] << endl;
	}
};

int main() {
	One o;
	o.setNum();
	o.solution();
	o.printNum();
	return 0;
}