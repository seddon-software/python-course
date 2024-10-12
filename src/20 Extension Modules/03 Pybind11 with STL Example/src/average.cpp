#include <vector>


int average(std::vector<int> v)
{
    int sum = 0;
    for(unsigned i = 0; i < v.size(); i++)
    {
        sum += v[i];
    }
    return sum / v.size();
}

double average2(std::vector<double> v)
{
    double sum = 0;
    for(unsigned i = 0; i < v.size(); i++)
    {
        sum += v[i];
    }
    return sum / v.size();
}

