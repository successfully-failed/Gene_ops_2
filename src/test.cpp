#include <iostream>

using namespace std;

void do_sth();

int do_a_thing()
{
	do_sth();
	return 1;
}

int main ()
{
	do_a_thing();
	return 0;
}
