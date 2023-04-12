class Solution:
    def simplifyPath(self, path: str) -> str:
        # Rules:
        # 1. Path starts with a single / -> insert / in the stack
        # 2. if char=='/' and st[-1]=='/': continue
        # 3. at the end if st[-1]=='/': st.pop()
        # 3.5 if char=='.': if st[-1].contains('.'): st[-1]+='.' else st.push('.')
        # 4. any other time if st[-1]=='.' or st[-1]=='..': st.pop()
        # print()
        stack = []
        directories = path.split("/")
        for dir in directories:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return "/" + "/".join(stack)