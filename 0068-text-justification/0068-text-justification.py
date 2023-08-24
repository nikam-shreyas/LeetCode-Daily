class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Step 1: Divide the words into lines
        # Step 2: Calculate the spaces (number of words - 1) and remaining space
        #   Step 2.1 If the spaces==0, then remaining_space will be put to the right of the word
        #   Step 2.2 apply ceil(remaining_spaces//spaces) after each word
        # Step 3: For the last line left justify it.
        words = deque(words)
        lines = []
        i=0
        len_curr_line = 0
        curr_line = []
        while words:
            curr_word = words.popleft()
            if len_curr_line+len(curr_word)>maxWidth:
                lines.append((curr_line, len_curr_line))
                curr_line = [curr_word]
                len_curr_line=len(curr_word)+1
            else:
                curr_line.append(curr_word)
                len_curr_line+=len(curr_word)+1
        lines.append(curr_line)
        
        ans = []
        
        for i in range(len(lines)-1):
            line, line_len = lines[i]
            # print(line, end=' ')
            remaining_spaces = maxWidth - line_len + 1
            num_words = len(line)
            if num_words==1:
                ans.append(line[0]+' '*(remaining_spaces))
                continue
            line_with_spaces = []
            num_spaces = len(line)-1
            for j in range(len(line)-1):
                word = line[j]
                # print(remaining_spaces, num_spaces, (ceil(remaining_spaces/num_spaces)))
                line_with_spaces.append(word)
                line_with_spaces.append(' ')
                line_with_spaces.append(' '*(ceil(remaining_spaces/num_spaces)))
                remaining_spaces-=ceil(remaining_spaces/num_spaces)
                num_spaces-=1
            line_with_spaces.append(line[-1])
            ans.append(''.join(line_with_spaces))
        last_line = ' '.join(lines[-1])
        last_line += ' '*(maxWidth-len(last_line))
        ans.append(last_line)
        # print([len(line) for line in ans])
        return ans
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                