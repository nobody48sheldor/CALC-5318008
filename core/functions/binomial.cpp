#include <iostream>

using namespace std;

int factorial(int x)
{
	int X = 1;
	for (int i = 1; i<=x; i++)
	{
		X = X*i;
	}
	return X;
}

double pow(double x, int y)
{
	double X = 1;
	for (int i = 1; i <= y; i++)
	{
		X = X*x;
	}
	return X;
}

double proba(int n, double p, int k)
{
	double X = (factorial(n)/(factorial(k)*factorial(n-k))) * pow(p, k) * pow(1-p, n-k);
	return X;
}

int main(int n[], double p)
{
	cout << n[0] << endl;
	cout << p << endl;
	cout << n[1] << endl;
	double x = pow(2, 5);
	double y = factorial(3);
	double P = proba(n[0], p, n[1]);
	return P;
}
