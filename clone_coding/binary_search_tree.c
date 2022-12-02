#include <stdio.h>
#include <stdlib.h>

//노드 구조체
typedef struct _Node {
    int key;
    struct _Node* left;
    struct _Node* right;
} Node;

//노드 검색
Node *search(Node *root, int x) {
    Node *p = root;
    //노드가 NULL이 아니라면 계쏙해서 검색을 시도한다.
    while (p != NULL) {
        //해당 값을 찾았다면 해당 노드를 리턴.
        if (p->key == x) return p;
        //못 찾았다면 현재 검색 하고 있는 노드의 크기를 비교한다.
        //검색 하고 싶은 값이 해당 노드보다 크다면 오른자식, 작다면 왼자식으로 이동.
        if (p->key < x){
            p = p->right;
        }else{
            p = p->left;
        }
    }
    //끝까지 못찾았다면 검색 값이 존재하지 않기 때문에 NULL 리턴
    return NULL;
};

//노드 삽입
Node *insert(Node *root, int x) {
    Node *p = root;
    Node *parent = NULL;
    //부모 노드를 찾는다.
    while (p != NULL) {
        parent = p;
        //이진탐색트리는 중복값이 존재 하면 안되기 때문에 중단.
        if (p->key == x) {
            printf("같은 키가 존재\n");
            return p;
        }
        if (p->key < x) {
            p = p->right;
        }else{
            p = p->left;
        }
    }
    //삽일 할 노드 선언
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->key = x;
    //삽입 노드는 항상 최 하단에 삽입되기 때문에 자식노드가 없다.
    newNode->left = newNode->right = NULL;

    //삽입되는 위치가 부모노드의 오른쪽인지 왼쪽인지 확인
    if (parent != NULL) {
        if (parent->key < newNode->key) {
            parent->right = newNode;
        }else {
            parent->left = newNode;
        }
    }
    return newNode;
}

//노드 삭제
Node *delete(Node *root, int x) {
    Node *p = root;
    Node *parent = NULL;
    //삭제할 노드를 찾는다.
    while ((p != NULL) && (p->key == x)) {
        parent = p;
        if (p->key < x) {
            p = p->right;
        }else {
            p = p->left;
        }
    }
    if (p == NULL) {
        printf("찾는 노드가 없습니다.\n");
        return root;
    }
    //차수가 0인 경우
    if ((p->left == NULL) && (p->right == NULL)) {
        if (parent == NULL){
            root = NULL;
        }else {
            if (parent->left == p) {
                parent->left = NULL;
            }else {
                parent->right = NULL;
            }
        }
    }
    //차수가 1인 경우
    else if ((p->left == NULL) || (p->right == NULL)) {
        Node* child = (p->left != NULL) ? p->left : p->right;
        if (parent == NULL) {
            root = child;
        }else {
            if (parent->left == p) {
                parent->left = child;
            }else {
                parent->right = child;
            }
        }
    }
    //차수가 2인 경우
    else {
        Node* successor_parent = p;
        Node* successor = p->right;
        while (successor->left != NULL) {
            successor_parent = successor;
            successor = successor->left;
        }
        p->key = successor->key;
        if (successor_parent->left == successor) {
            successor_parent->left = successor->right;
        }else {
            successor_parent->right = successor->left;
        }
        p = successor;
    }
    free(p);
    return root;
}


void Inorder(Node * root){
    if (root == NULL){
        return;
    }
    Inorder(root->left);
    printf("%d \n", root->key);
    Inorder(root->right);
}

int main() {
    Node* root = insert(NULL, 43);
    insert(root, 34);
    insert(root, 52);
    insert(root, 72);
    insert(root, 12);
    insert(root, 54);
    Inorder(root);
    return 0;
}