with open("facebook_no_k.bat", "w") as f:
    f.write("python main.py facebook -no-labels --iterations 3000 --draw")
with open(f"communities_louvain_draw.bat", mode="w") as f:
    f.write("python ../main.py communities louvain -no-labels --iterations 3000 --draw")
for i in range(1, 9):
    with open(f"facebook_k_{i}.bat", mode="w") as f:
        f.write("python ../main.py facebook --k {} -no-labels --iterations 3000 --draw".format(i))
    with open(f"communities_kcliques_{i}.bat", mode="w") as f:
        f.write("python ../main.py communities kcliques --k {}".format(i))
    with open(f"communities_kspanningTree_{i}.bat", mode="w") as f:
        f.write("python ../main.py communities kspanningtree --k {}".format(i))
with open(f"communities_louvain.bat", mode="w") as f:
    f.write("python ../main.py communities louvain")
print("done")
