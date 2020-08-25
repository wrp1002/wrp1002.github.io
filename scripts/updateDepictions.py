import json
import os

projectPath = os.path.join(os.path.expanduser("~"), "Documents/projects/")
depictionPath = os.path.join(os.path.expanduser("~"), "Documents/repo/depictions")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
blacklistedFiles = ["ideas"]

#=========================================================================================

def GetScreenshots(d):
	screenshotTemplate = '<img class="img_card" src="%screenshot%">'
	screenshots = ""
	for s in d:
		screenshots += screenshotTemplate.replace("%screenshot%", s)
	return screenshots

def GetChangelog(d):
	changelogTemplate  = """
					<li>
						<b>%version%</b><br>
%changes%
					</li>"""

	changelog = ""
	for item in reversed(d):
		version = item["version"]
		changes = ""
		for change in item["changes"]:
			changes += "						- " + change + "<br>\n"

		changelog += changelogTemplate.replace("%version%", version).replace("%changes%", changes)
	return changelog

functions = {"screenshots": GetScreenshots, "changelog": GetChangelog}

#=========================================================================================

def MakeDepiction(f):
	try:
		with open("depictionTemplate.html") as file:
			template = file.read()

		with open(f) as file:
			data = json.loads(file.read())

		#print(data)

		for key in data:
			if key in functions:
				template = template.replace("%"+key+"%", functions[key](data[key]))
			else:
				template = template.replace("%"+key+"%", str(data[key]))

		return template
	except:
		print("Warning:", f, "not found")
		return ""

def GetTweakName(f):
	try:
		with open(f) as file:
			data = json.loads(file.read())
		
		return data["title"]

	except:
		return ""



def main():
	names = [f for f in os.listdir(projectPath)]

	for b in blacklistedFiles:
		if b in names:
			names.remove(b)
		else:
			print("Warning: blacklisted item '" + b + "' not found")

	print("Tweaks found:", names)

	for name in names:
		depiction = MakeDepiction(os.path.join(projectPath, name, "depiction.json"))
		if depiction:
			tweakName = GetTweakName(os.path.join(projectPath, name, "depiction.json"))

			tweakDir = os.path.join(depictionPath, tweakName)
			if not os.path.exists(tweakDir):
				os.makedirs(tweakDir)

			with open(os.path.join(tweakDir, "index.html"), 'w') as file:
				print("Writing to", os.path.join(tweakDir, "index.html"))
				file.write(depiction)



if __name__ == "__main__":
	main()