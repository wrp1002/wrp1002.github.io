import os
import sys
from os.path import isfile, join

template = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>wrp1002's Repo</title>
		<link rel="icon" href="/CydiaIcon.png">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="./depictions/resources/css/style.css">
	</head>


	<body ontouchstart="">
		<div class="title">wrp1002's Repo</div>

		<main id="content" role="main">
			<div>
				<a href="cydia://url/https://cydia.saurik.com/api/share#?source=https://wrp1002.github.io/" class="repoButton">Add repo to Cydia</a>
				<a href="zbra://sources/add/https://wrp1002.github.io" class="repoButton">Add repo to Zebra</a>
			</div>

			<br>

			<div class="headingCenter">My Tweaks</div>

			<ul>
%LINKS%
			</ul>


			<div class="headingCenter">Info</div>
			<ul>
				<li>
					<a href="http://github.com/wrp1002" target="_blank" role="button">Github<img height="28" width="28" src="depictions/resources/github.png"></a>
				</li>
			</ul>
		</main>
	</body>
</html>
"""

linkTemplate = '				<li><a href="./depictions/%TWEAKNAME%/index.html" role="button">%TWEAKNAME% <img height="24" width="24" src="depictions/%TWEAKNAME%/icon.png"></a></li>\n'


os.chdir(os.path.dirname(os.path.abspath(__file__)))


blacklistedFiles = ["resources"]
links = ""
names = [f for f in os.listdir("../depictions")]

for b in blacklistedFiles:
	names.remove(b)

print("Tweaks found:", ", ".join(names))

for name in names:
	links += linkTemplate.replace("%TWEAKNAME%", name)

finalPage = template.replace("%LINKS%", links)

#print(finalPage)

print("Writing to index.html... ", end="")
with open("../index.html", 'w+') as file:
	file.write(finalPage)
print("Done")

