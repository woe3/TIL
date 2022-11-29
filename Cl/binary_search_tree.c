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
    while (p != NULL) {
        if (p->key == x) return p;
        if (p->key < x){
            p = p->right;
        }else{
            p = p->left;
        }
    }
    return NULL;
};

//노드 삽입
Node *insert(Node *root, int x) {
    Node *p = root;
    Node *parent = NULL;
    while (p != NULL) {
        parent = p;
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
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->key = x;
    newNode->left = newNode->right = NULL;

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