" delete first 8 lines because they have no annotations
1,8d
" extract highlights as strings
%s/^"Highlight.*,"\(.*\)"$/\1/ 
" extract notes between comment notation
%s/^"Note.*,"\(.*\)"$/\/* \1 *\/ 
" add one empty line between each line 
g/$/s/$/\r 
" format entire file to max 80 characters wide
norm gggqG 
" save file
write kindle_highlights.md
" quit without saving the original csv file
q!
