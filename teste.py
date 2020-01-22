import os

a = "dmidecode -t 17 | awk '"
b = 'BEGIN { FS=":"; OFS="\t" } /Size|Locator|Type:|Speed|Manufacturer|Serial Number|Part Number/ { gsub(/^[ \t]+/,"",$2); line = (line ? line OFS : "") $2 } /^$/ { print line; line="" }'
c = "' | grep -iv "
d = '"no module"'
command = '' . join(a + b + c + d)
resultado =  os.popen(command).read()
print(resultado)


# comando puro
# dmidecode -t 17 | awk 'BEGIN { FS=":"; OFS="\t" } /Size|Locator|Type:|Speed|Manufacturer|Serial Number|Part Number/ { gsub(/^[ \t]+/,"",$2); line = (line ? line OFS : "") $2 } /^$/ { print line; line="" }' | grep -iv "no module"