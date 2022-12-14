/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "ateam",
    /* First member's full name */
    "Harry Bovik",
    /* First member's email address */
    "bovik@cs.cmu.edu",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};

#define WSIZE 4 //  Word and header / footer size(bytes)
#define DSIZE 8 //  Double word size(bytes)
#define CHUNKSIZE (1<<12) // Extend heap by this amount

#define MAX(x,y) ((x)>(y)?(x):(y))

// Pack a size and allocated bit into a word
#define PACK(size,alloc) ((size)|(alloc))

// Read and write a word at address
#define GET(p) (*(unsigned int *)(p))
#define PUT(p,val) (*(unsigned int*)(p)=(val))

// Read the size and allocated fields from address p
#define GET_SIZE(p) (GET(p) & ~0x7)
#define GET_ALLOC(p) (GET(p) & 0x1)

//Given block ptr bp, compute address of its header and footer
#define HDRP(bp) ((char *)(bp)-WSIZE)
#define FTRP(bp) ((char *)(bp)+GET_SIZE(HDRP(bp))-DSIZE)

//Given block ptr bp, compute address of next and previous blocks
#define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE(((char *)(bp - WSIZE))))
#define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE(((char *)(bp - DSIZE)))) 

// 이전의 가용블록의 위치를 저장하는 포인터를 저장하는 포인터
#define SUCC_P(bp)  (*(void **)(bp))

// 다음의 가용블록의 위치를 저장하는 포인터를 저장하는 포인터
#define PRED_P(bp)  (*(void **)((bp)+WSIZE))


/* single word (4) or double word (8) alignment */
#define ALIGNMENT 8

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~0x7)

#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

static void *coalesce(void *bp);
static void *extend_heap(size_t words);
static void *find_fit(size_t size);
static void place(char* bp, size_t size);

static void list_add(char* bp);
static void list_remove(char* bp);

static char* heap_listp;
/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{
    if((heap_listp = (char*)mem_sbrk(6*WSIZE)) == (void *)-1) return -1;
	
    PUT(heap_listp,0);                                  // Alignment padding
    PUT(heap_listp + (1*WSIZE), PACK(2*DSIZE,1));       // Prologue header  -> why 2*DSIZE ??? 헤더,푸터, 가용리스트를 가리키는 포인터(두개!) 
    PUT(heap_listp + (2*WSIZE), heap_listp+(2*WSIZE));  // 이전 가용 리스트 블록을 가리키는 포인터
    PUT(heap_listp + (3*WSIZE), heap_listp+(3*WSIZE));  // 다음 가용 리스트 블록을 가리키는 포인터
    PUT(heap_listp + (4*WSIZE), PACK(2*DSIZE,1));       // Prologue Footer
    PUT(heap_listp + (5*WSIZE), PACK(0,1));             // Epilogue header
    heap_listp += (2*WSIZE);
    
    
    // Extend the empty heap with a free block of CHUNKSIZE bytes
    if (extend_heap(CHUNKSIZE/WSIZE) == NULL) return -1;
    
    return 0;
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    // int newsize = ALIGN(size + SIZE_T_SIZE);
    // void *p = mem_sbrk(newsize);
    // if (p == (void *)-1)
	// return NULL;
    // else {
    //     *(size_t *)p = size;
    //     return (void *)((char *)p + SIZE_T_SIZE);
    // }

    size_t asize;           // Adjusted block size
    size_t extendsize;      // Amount to extend heap if no fit
    char *bp;

    // Ignore spurious requests
    if (size == 0) return NULL;

    // Adjust block size to include overhead and alignment reqs
    if (size <= DSIZE)
        asize = 2*DSIZE;
    else
        asize = DSIZE * ((size + (DSIZE) + (DSIZE-1))/DSIZE);
    
    // Search the free list for a fit
    if ((bp = find_fit(asize)) != NULL){
        place(bp,asize);
        return bp;
    }

    // No fit found. Get more memory and place the block
    extendsize = MAX(asize,CHUNKSIZE);
    if((bp = extend_heap(extendsize/WSIZE)) == NULL) return NULL;
    place(bp,asize);
    return bp;


}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
    size_t size = GET_SIZE(HDRP(ptr));

    PUT(HDRP(ptr), PACK(size,0));
    PUT(FTRP(ptr),PACK(size,0));
    coalesce(ptr);
}

void *coalesce(void *bp){
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    // case 1
    if (prev_alloc && next_alloc){
        list_add(bp);
        return bp;
    } 

    // case 2  
    else if(prev_alloc && !next_alloc) {
        list_remove(NEXT_BLKP(bp));
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp),PACK(size,0));
        PUT(FTRP(bp),PACK(size,0));
    }
    // case 3
    else if(!prev_alloc && next_alloc){
        list_remove(PREV_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        PUT(FTRP(bp), PACK(size,0));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size,0));
        bp = PREV_BLKP(bp);
    }
    // case 4
    else{
        list_remove(NEXT_BLKP(bp));
        list_remove(PREV_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp)));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size,0));
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size,0));
        bp = PREV_BLKP(bp);

    }
    list_add(bp);
    return bp;
}


/*
* 루트 바로 뒤(오른쪽)에 새로운 가용 블록을 연결해줌
*/ 
void list_add(char* bp)
{
    SUCC_P(bp) = SUCC_P(heap_listp);
    PRED_P(bp) = heap_listp;
    PRED_P(SUCC_P(heap_listp)) = bp;
    SUCC_P(heap_listp) = bp;

}

/*
* 루트 바로 뒤(오른쪽)에 새로운 가용 블록을 연결해줌
*/ 
void list_remove(char* bp)
{
    PRED_P(SUCC_P(bp)) = PRED_P(bp);
    SUCC_P(PRED_P(bp)) = SUCC_P(bp);
}

void *mm_realloc(void *bp, size_t size){
    // 예전 사이즈 받아옴
    size_t old_size = GET_SIZE(HDRP(bp));
    // 새로운 사이즈 할당(DSIZE는 헤더와 풋터)
    size_t new_size = size + (DSIZE);


    // 만약 새로운 사이즈가 이전 사이즈보다 작거나 같은 경우
    if(new_size <= old_size){
        // 기존의 bp 반환
        return bp;
    }
    // 만약 새로운 사이즈가 이전 사이즈보다 큰 경우
    // 사이즈 변경
    else{
        // 다음 블록의 할당 상태를 받아옴
        size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
        // 다음 블록의 사이즈를 받아옴
        size_t current_size = old_size + GET_SIZE(HDRP(NEXT_BLKP(bp)));

        // 다음 블록이 가용 상태이고, 다음 블록의 사이즈의 합이
        //새로운 사이즈보다 크면
        // 바로 합쳐서 할당
        if(!next_alloc && current_size >= new_size){
            // 할당 상태로 헤더 추가
            list_remove(NEXT_BLKP(bp));
            PUT(HDRP(bp), PACK(current_size, 1));
            // 할당 상태로 풋터 추가
            PUT(FTRP(bp), PACK(current_size, 1));
    
            // 기존의 bp 반환
            return bp;
        }
        // 새로 블록 만들어서 옮기기
        else{
            // 새로운 사이즈로 new bp 할당
            void *new_bp = mm_malloc(new_size);
            if (new_bp == NULL) return NULL;
            // 새로운 bp에 새로운 사이즈로 가용 블록 분항
            // place(new_bp, new_size);
            // 메모리의 특정한 부분으로부터 얼마까지의 다른 메모리 영역으로 복사해주는 함수
            // 이전 bp로부터 사이즈만큼의 문자를 새로운 bp에 복사하라
            // memcpy(new_bp, bp, new_size);
            memmove(new_bp, bp, new_size);
            // 이전 bp free
            mm_free(bp);
            // 새로운 bp 반환
            return new_bp;
        }
    }
}


// void *mm_realloc(void *ptr, size_t size)
// {
//     void *oldptr = ptr;
//     size_t copySize;
//     // adjust block size to include overhead and aligment reqs.
//     size_t new_size;
//     if(size <= DSIZE)
//         new_size = 2 * DSIZE;
//     else{
//         new_size = DSIZE * ((size + (DSIZE) + (DSIZE - 1)) / DSIZE);
//     }
//     // (size/WSIZE % 2) ? (size/WSIZE + 1) * WSIZE : size/WSIZE * WSIZE;
//     //새로 할당할 사이즈가 본래 사이즈보다 작거나 같을 때
//     //즉시 반환
//     copySize = GET_SIZE(HDRP(oldptr));
//     if (new_size <= copySize)
//         return oldptr;

//     // 사이즈가 본래 사이즈 보다 크고, 다음 블럭이 가용 블럭 일 경우
//     size_t size_sum = GET_SIZE(HDRP(NEXT_BLKP(oldptr))) + GET_SIZE(HDRP(oldptr));
//     if (!GET_ALLOC(HDRP(NEXT_BLKP(oldptr))) && size_sum >= new_size)
//     {
//         if (size_sum - new_size < 2*DSIZE)
//         {
//             PUT(HDRP(oldptr), PACK(size_sum, 1));
//             PUT(FTRP(oldptr), PACK(size_sum, 1));
//         }else{
//             PUT(HDRP(oldptr), PACK(new_size, 1));
//             PUT(FTRP(oldptr), PACK(new_size, 1));
//             oldptr = NEXT_BLKP(oldptr);
//             PUT(HDRP(oldptr), PACK(size_sum - new_size, 0));
//             PUT(FTRP(oldptr), PACK(size_sum - new_size, 0));
//         }
//         return ptr;
//     }

//     // 일반적인 raalloc 함수
//     // malloc을 이용해서 새로운 사이즈를 할당하고 할당된 곳에
//     // 데이터를 이전해서 보존한 이후, 본래 할당된 메모리를 가용 메모리로 전환
//       // 새로운 사이즈로 new bp 할당
//             void *new_bp = mm_malloc(new_size);
//             if (new_bp == NULL) return NULL;
//             // 새로운 bp에 새로운 사이즈로 가용 블록 분항
//             // place(new_bp, new_size);
//             // 메모리의 특정한 부분으로부터 얼마까지의 다른 메모리 영역으로 복사해주는 함수
//             // 이전 bp로부터 사이즈만큼의 문자를 새로운 bp에 복사하라
//             // memcpy(new_bp, bp, new_size);
//             memmove(new_bp, oldptr, new_size);
//             // 이전 bp free
//             mm_free(oldptr);
//             // 새로운 bp 반환
//             return new_bp;
// }
void *extend_heap(size_t words){
    char *bp;
    size_t size;

    //Allocate an even number of words to maintain alignment
    size = (words%2) ? (words+1) * WSIZE : words * WSIZE;
    if((long)(bp = mem_sbrk(size))== -1) return NULL;

    // Initialize free block header/footer and the epilogue header
    PUT(HDRP(bp), PACK(size,0));                 // Free block header
    PUT(FTRP(bp),PACK(size,0));                  // Free block footer
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0,1));          // New epilogue header
    
    // Coalesce if the previous block was free
    return coalesce(bp);

}

// Root의 다음 가용블록을 찾아다니면서 인자로 전달받은 사이즈보다 
// 큰 사이즈의 가용블록 사이즈가 존재한다면  해당 주소를 리턴해준다.
void *find_fit(size_t size)
{   
    char *bp;
    for (bp = SUCC_P(heap_listp); !GET_ALLOC(HDRP(bp)); bp = SUCC_P(bp)) 
        if(GET_SIZE(HDRP(bp)) >= size)
            return bp;
    
    return NULL;
}

void place(char* bp, size_t size){

    size_t c_size = GET_SIZE(HDRP(bp));
    // 기존의 가용블록을 잘라서 사용할 것이기 때문에 연결 잘라줌
    list_remove(bp);

    if (c_size - size >=(2*DSIZE)){
            PUT(HDRP(bp),PACK(size,1));
            PUT(FTRP(bp),PACK(size,1));
            bp = NEXT_BLKP(bp);
            PUT(HDRP(bp),PACK(c_size-size,0));
            PUT(FTRP(bp),PACK(c_size-size,0));
            // 새로생긴 가용블록을 Root 앞에 붙여줌
            list_add(bp);
    }
    else{
        PUT(HDRP(bp),PACK(c_size,1));
        PUT(FTRP(bp),PACK(c_size,1));
    }
}










