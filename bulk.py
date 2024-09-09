import os
import glob
import subprocess

pwd = os.path.join(os.getcwd(), "**/*")

hb_cmd = "HandBrakeCLI --all-subtitles --all-audio --quality 22.0 --encoder nvenc_h265_10bit --detelecine --vfr --hqdn3d=strong --chroma-smooth=verystrong"

file_list = [f for f in glob.iglob(pwd, recursive=True) if os.path.isfile(f)]

for f in file_list:
    if not f.endswith(".mkv"):
        continue
    f_tok = f.split("/")
    o_str = ""
    for ind, tok in enumerate(f_tok):
        if ind == 0:
            continue
        o_str += "/"
        if ind == f_tok.__len__() - 1:
            o_str += "z_"
        o_str += tok
    cmd = hb_cmd + " -i " + "'" + f + "'" + " -o " + "'" + o_str + "'"
    print(cmd)
    process = subprocess.Popen(cmd, shell=True)
    _ = process.wait()
    print(process.returncode)

