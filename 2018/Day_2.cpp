#include <bits/stdc++.h>
using namespace std;

int twosCount;
int threesCount;

char input[26];
vector<string> boxes;
string boxID;

//PART 1
void count(string boxID) {
	//init
	int count[26];
	for (int i=0; i<26; i++){
		count[i] = 0;
	}
	//count frequency
	for (auto letter:boxID){
		count[letter-'a']++;
	}
	//produce answer
	int index = 0;
	int hasTwo = 0;
	int hasThree = 0;
	while (index < 26) {
		if (!hasTwo){
			if (count[index] == 2) { twosCount++; hasTwo = 1;}
		}
		if (!hasThree){
			if (count[index] == 3) { threesCount++; hasThree = 1;}
		}
		index++;
	}
}

//PART 2
void commonLetters() {
	int found = 0;
	for (auto ID1:boxes) {
		for (auto ID2:boxes) {
			//count differing letters
			int differentL = 0;
			for (int i=0; i<26; i++) {
				if (ID1[i] != ID2[i]) {differentL++;}
			}
			if (differentL == 1 && !found) {
				found = 1;
				//print the two common letters
				for (int i=0; i<26; i++) {
					if (ID1[i] == ID2[i]) {printf("%c",ID1[i]);}
				}
				printf("\n");
			}
		}
	}
}

int main(){
	freopen("day2in.txt","r",stdin);

	while (1) {
		int returned = scanf("%s",input);
		boxID = input;
		if (returned != 1) {
			//EOF reached
			break;
		}
		boxes.push_back(boxID);
		count(boxID);
	}
	
	//printf("%d %d\n", twosCount, threesCount);
	printf("%d\n", twosCount*threesCount);
	commonLetters();
}


