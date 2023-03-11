class Solution {
public:
string sortSentence(string s) {
// using the ascii value 0-9 in ascii==48-57
string word, arr;
vector<string>v(10);
for(int i=0;i<s.size();i++)
{
if(s[i]>=48&& s[i]<=57){
v[s[i]-48]=word+" ";
word="";
i++;
}
​
else
word+=s[i];
}
for(string a: v)
{
arr+=a;
}
arr.pop_back();
return arr;
}
};