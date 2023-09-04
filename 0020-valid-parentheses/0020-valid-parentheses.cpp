#include<stack>
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        st.push('#');
        for(char c:s){
            if(c=='(' || c=='[' || c=='{'){
                st.push(c);
            }
            else if(c==')'){
                if(st.top()!='('){
                    return false;
                }
                else{
                    st.pop();
                }
            }
            else if(c==']'){
                if(st.top()!='['){
                    return false;
                }
                else{
                    st.pop();
                }
            }
            else if(c=='}'){
                if(st.top()!='{'){
                    return false;
                }
                else{
                    st.pop();
                }
            }
        }
        if(st.top()=='#'){
            return true;
        }
        return false;
    }
};