with open("facebook_no_k.bat", "w") as f:
    f.write("python main.py facebook -no-labels --")
for i in range(1, 9):
    with open(f"facebook_k_{i}.bat", mode="w") as f:
        f.write("python ../main.py facebook --k {} -no-labels --iterations 3000".format(i))
for i in range(1, 9):
    with open(f"communities_fluid_{i}.bat", mode="w") as f:
        f.write("python ../main.py communities fluid --k {} -no-labels --iterations 3000".format(i))
for i in range(1, 9):
    with open(f"communities_louvain_{i}.bat", mode="w") as f:
        f.write("python ../main.py communities louvain --k {} -no-labels --iterations 3000".format(i))

with open("../communities.bat", mode="w") as f:
    f.write("start bats/facebook_no_k.bat\n")
    for i in range(1, 9):
        f.write("start bats/facebook_k_{}.bat\n".format(i))
    for i in range(1, 9):
        f.write("start bats/communities_fluid_{}.bat\n".format(i))
    for i in range(1, 9):
        f.write("start bats/communities_louvain_{}.bat\n".format(i))