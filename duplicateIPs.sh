for x in $(cat file1.txt | cut -d ":" -f 1); do
    grep $x file2.txt | cut -d ":" -f 1
done
