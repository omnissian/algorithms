
#include "pch.h"
#include <iostream>
#include <math.h>
#include<time.h>


void array_fill(int *array,int size, int left_boud, int right_bound) {
	for (; size >= 0; --size) {
		*(array + size) = rand() % right_bound + left_boud;

	}
	return;
}

void swap(int *left,int *right){
	if (left != right) {
		*left += *right;
		*right = *left - *right;
		*left = *left - *right;
	}
	return;

}
void cout_array(int *array, int size) {
	for (int i = 0; i < size; i++) {
		std::cout << array[i] << ", ";
	}
	std::cout << std::endl;
}
//
//void cout_1(auto var) {
//
//}


void quick_sort(int *array, int size) { /* array - points on the "left", first element, size - number of the ements*/
	//int id_pivot = rand() % size;
	std::cout << "----->new function call----->" << std::endl;
	std::cout << "array before sort:" << std::endl;
	cout_array(array, size);
	if(size>2) {
		int id_pivot = rand() % size; // 0=< to <size
		
		int * left = array+1;
		int * right = array + (size-1);
		swap(array, array + id_pivot);
		std::cout<<"pivot value is "<<*array <<std::endl;
		//std::cout<< <<std::endl;
		for (;left<right;) {
			if (*left >= *array) {
				if (*right <= *array) {
					swap(left, right);
					left++;
					right--;
				}
				else {
					right--;
				}
			}
			else {
				left++;
			}

		}
		if (*left >= *array) {
			swap(--left, array);
		}
		else {
			swap(left, array);
		}

		std::cout << "array after sort:" << std::endl;
		cout_array(array, size);
		return quick_sort(array,left-array), quick_sort(left + 1, size - (left - array)-1);

	}
	else if (size == 2) {
		if (*array > *(array + 1)) {
			swap(array, array + 1);
			return;
		}
	}
	else {
		return;
	}
	std::cout << "array after pivot sort:" << std::endl;
	cout_array(array, size);

	std::cout << "debug point" << std::endl;
	return;
}

const int size = 10;
int main()
{
	srand(time(NULL));
	int array[size];
	//int array[size] = { 77,88, 76,93,7,50,42,4,61,44 };
	array_fill(array, size, 0, 100);
	std::cout << "before sort" << std::endl;
	for (int i = 0; i < size; i++) {
		std::cout << array[i]<<", ";
	}
	std::cout <<  std::endl;
	std::cout << "------sort started---------"<<std::endl;
	quick_sort(array,size);
	std::cout << "after sort" << std::endl;
	cout_array(array, size);





    std::cout << "Hello World!\n"; 
}
