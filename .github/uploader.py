from os import system as run, listdir, remove
from json import load
import tgconfig

with open("../.github/commit.json") as f:
    data = load(f)

message = f"Commit {data['sha'][:7]}, signed off by: {data['commit']['author']['name']}"

files, signed_files, unsigned_files = listdir(), [], []
for file in files:
    if file.endswith("signed.apk"):
        signed_files.append(file)
    elif file.endswith(".apk"):
        unsigned_files.append(file)

if len(signed_files):
    for file in unsigned_files:
        remove(file)

if tgconfig.GH_REPO.lower() == "libre-tube/libretube":
    run("git add -f *")
    run(f"git commit -m \"{message}\"")
    run("git push -u")
else:
    print("Official Repo not Detected")
