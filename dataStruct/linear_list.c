//
// Created by lwz on 18-8-27.
//

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

//ADT List{
//    InitList(& L);
//    DestoryList(&L);
//    ClearList(&L);
//    ListEmpty(L); // check if empty
//    ListLength(L); // list length
//    GetElem(L, i, &e); // use e to store the value of l[i]
//    LocateElem(L, e, compare()); // locate
//    PriorElem(L, cur_e, &pre_e); // cur_e's prior
//    NextElem(L, cur_e, &next_e);
//    ListInsert(&L, i, e); // insert new  in L before ith
//    ListDelete(&L, i, &e); //delete L[i] and return the value
//    ListTraverse(L, visit()); // visit all element in L
//}ADT List;
//
//void union(List &La, List Lb);
//void Merge();

#define LIST_INIT_SIZE 100
#define LIST_INCREMENT 10
#define ElemType int
typedef struct {
    ElemType * elem; // storage space
    int length;
    int listsize; // sizeof(ElemType
}SqList;

Status InitList_Sq(SqList &L){
}
