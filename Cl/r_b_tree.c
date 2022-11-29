#include <stdio.h>
#include <stdlib.h>

//노드 구조체
// key, color, parent, left_child, right_child
typedef struct _node {
    int key;
    enum {red, Black} color;

    struct _node* parent;
    struct _node* left;
    struct _node* right;
} node;

node* search()