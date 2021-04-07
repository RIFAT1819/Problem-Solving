/*Bismillahhir Rahmanir Rahim*/
/*Ahamed Imtiaz Rifat*/
/*Varendra University*/


#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s,stop="the end.";
    for(;getline(cin,s);)
    {
        if(s==stop)
            break;
        for(int i=0; s[i]!='\0'; i++){
            if(s[i]=='6')
                s[i]='b';
            else if(s[i]=='9')
                s[i]='g';
            else if(s[i]=='1')
                s[i]='l';
            else if(s[i]=='0')
                s[i]='o';
            else if(s[i]=='5')
                s[i]='s';
            else if(s[i]=='2')
                s[i]='z';
            else if(s[i]=='b')
                s[i]='6';
            else if(s[i]=='g')
                s[i]='9';
            else if(s[i]=='l')
                s[i]='1';
            else if(s[i]=='o')
                s[i]='0';
            else if(s[i]=='s')
                s[i]='5';
            else if(s[i]=='z')
                s[i]='2';
        }
        cout<<s<<endl;
    }
    return 0;
}
