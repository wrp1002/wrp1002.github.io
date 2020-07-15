
#!/bin/sh
rm Packages.bz2
{ for fn in debs/*; do
  ar p "$fn" control.tar.gz | tar xzO ./control
  echo Filename: "$fn"
  echo Size: $(stat -c%s "$fn")
  echo MD5sum: $(md5sum "$fn" | cut -d" " -f1)
  echo SHA1: $(sha1sum "$fn" | cut -d" " -f1)
  echo SHA256: $(sha256sum "$fn" | cut -d" " -f1)
  echo Depiction: https://wrp1002.github.io/depiction/"$fn"/index.html | sed "s/com.wrp1002.//g" | sed "s/.deb//g"
  echo
done } | tee Packages
bzip2 -f Packages
#read -p "Press enter to continue"
