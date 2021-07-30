#include <math.h>
#include "sumOfRoots.h"

double sumOfRoots(int n)
{
    double sum = 0.0;
    for(int i = 0; i < n; i++)
    {
        sum += sqrt((double)i);
    }
    return sum;
}

