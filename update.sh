
#!/bin/sh
packages=$(find ../projects/ -maxdepth 2 -name "packages" -type d)
projectFolders=$(find ../projects/ -maxdepth 1 -mindepth 1 -type d -name "*")

echo "Clearing debs folder..."
rm ./debs/*
echo ===========================================================================

echo "Clearing package folders..."
for p in $packages; do
	echo clearing $p
	rm $p/*
done
echo ===========================================================================

for p in $projectFolders; do
	echo "making package" $p
	make package -C $p
	echo
done
echo ===========================================================================

for p in $packages; do
	echo copying deb from $p
	cp $p/* ./debs
done
echo ===========================================================================
 
echo Updating packages file...
echo

rm Packages.bz2
{ for fn in debs/*; do
  ar p "$fn" control.tar.gz | tar xzO ./control
  echo Filename: "$fn"
  echo Size: $(stat -c%s "$fn")
  echo MD5sum: $(md5sum "$fn" | cut -d" " -f1)
  echo SHA1: $(sha1sum "$fn" | cut -d" " -f1)
  echo SHA256: $(sha256sum "$fn" | cut -d" " -f1)
  echo Depiction: https://wrp1002.github.io/depiction/"$fn"/index.html | sed "s/com.wrp1002.//g" | sed "s/.deb//g" | sed 's;_.*\/;/;g'
  echo
done } | tee Packages
bzip2 -f Packages

echo ===========================================================================
printf "Push to git? (y/n) "
read input

if [ $input == 'y' ]; then
	printf "Commit message: "
	read msg

	git add .
	git commit -m "$msg"
	git push
fi

