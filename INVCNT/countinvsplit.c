#include<stdio.h>
#include<stdlib.h>



#define DEBUG 0

long long int countInvMerge(int arr[], int start, int middle, int end)

{

    int sz= end-start+1;

    int i=0, j = 0, k = 0;
    long long int  countInv = 0;

    int *tmpArr =  (int *)malloc(sz * sizeof(int));

    if(tmpArr == NULL)

    {

      printf("TempArr Memory alloc failed\n");

      return 0;

    }

    for(i=start, j= middle+1; i<=middle && j <= end; )

    {

       if(arr[i] <= arr[j])

          tmpArr[k++] = arr[i++];

       else

       {

          tmpArr[k++] = arr[j++];

          countInv+=(middle-i+1);

       }

    }

    while(i<=middle)

       tmpArr[k++] = arr[i++];

    for(i = start ; i <=start+k-1; i++)

    {

       arr[i] = tmpArr[i-start];

    }

    #if DEBUG

    printf("\nMerged Arr\n");

    for(i= start; i<=end ; i++)

    {

       printf("%d\t", arr[i]);

    }

    #endif

    free(tmpArr);

    return countInv;

}



long long int countInvSplit(int arr[], int start, int end)

{

   long long int countInv = 0 ;

   long long int cLeft = 0,cRight = 0;

   int i = 0;

   if (end - start < 1)

       return 0 ;

   int middle = (start+end)/2;

   cLeft = countInvSplit(arr, start, middle);

   cRight = countInvSplit(arr, middle+1, end);

   

   countInv = countInvMerge(arr, start, middle, end);

   return cLeft + cRight + countInv;

}





#if 1

int main(void)

{

   int numList = 0, numElem = 0, i = 0;

   long long int countInv = 0 ;

   int *arr = NULL;

   scanf("%d", &numList);  

   if(numList <= 0) 

   {

  
     //printf("Invalid num of lists\n");

     return -1;

   }

   while(numList)

   {

      i = 0;

      scanf("%d", &numElem); 

      if(numElem <= 0)

      {

        printf("Invalid no of elems\n");

        numList--;

        continue;

      }

      numList--;
      arr = (int *)malloc(numElem * sizeof(int)); 

      if(arr == NULL)

      {

        printf("Array Memory alloc failed\n");

        return 0;

      }

      while(i < numElem)

      {

        scanf("%d", &arr[i]);
        if(arr[i] > 10000000)
        {
           //printf("-1\n");
           free(arr);
           return -1;
        }
        //printf("elem %d\n", arr[i]);

        i++;

      } 



      #if DEBUG

      printf("Original Array\n");

      for(i= 0; i<numElem ; i++)

      {

         printf("%d\t", arr[i]);

      }

      #endif

      countInv =  countInvSplit(arr, 0, numElem-1);

      #if DEBUG

      printf("\nTotal Count %lld\n", countInv);

      #endif
      printf("%lld\n", countInv);
      free(arr);

   }

}
#endif
