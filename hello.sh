 #!/bin/bash

declare -a stringArr=("User1" "User2" "User3")
a=2
b=2
c=$((a + b))
echo "Bash says: Hello, World!"
echo "$a + $b = $c"
for val in "${stringArr[@]}"; do
 echo "$val"
done
