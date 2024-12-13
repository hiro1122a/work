from Ex_1 import  team_names_2 ,modifiend_url,new_kickoff_time,url_suu,hiduke
template="""
"""
num_files=url_suu
hiduke_2,hiduke_3=hiduke.split("/")[0],hiduke.split("/")[1].split(" ")[0]
print(hiduke_2,hiduke_3)
for i in range(num_files):
    filename =  f"{hiduke_2}-{hiduke_3}_{team_names_2[i*2]}vs{team_names_2[i*2+1]}.py"
    with open(filename, "w",encoding="utf-8") as file:
        file.write(template.format(index=i))
    print(f"次の試合を作成 {filename}")