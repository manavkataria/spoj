#include <stdio.h>

#define DEBUG 0

#define dprint(str , args...) if (DEBUG) printf("%s:%d " str "\n",__FUNCTION__,__LINE__,  ##args); \
                                      else printf(str,  ##args)


int main(void)
{

    int N=0;        

    scanf("%d",&N);

    while(N!=42)
    {
        dprint("%d\n",N);
        scanf("%d",&N);
    }
        
    return 0;
}


