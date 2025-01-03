生成diff文件，首先需要将文件给展开使用latexpand main.tex > main_expand.tex 同样的新的文件也需要展开 ,然后在新的文件的目录下，使用latexdiff old_expand.tex(绝对路径) new_expand.tex > diff.tex,然后进行编译就可以了。
注意要生成展开文件，其次要注意使用的是绝对路径，最后要在新的文件夹下面进行编译
