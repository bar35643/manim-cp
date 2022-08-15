import ffmpeg
import os
import sys
import shutil



ROOT = os.getcwd()
print(ROOT)
if __name__ == '__main__': #python render.py .\projects\1-telepanting l
    path = f"{os.getcwd()}/{sys.argv[1]}"
    k=lambda x: int(x[1::].split('-')[0].split(' ')[0].split('.')[0])
    A = os.listdir(path)
    A = [x for x in A if x[0] == 'p']
    A.sort(key=k)
    q = sys.argv[2]
    qmap = {'l': '480p15', 'm': '720p30', 'h': '1080p60'}
    #s = "env PYTHONPATH=\"/Users/samuelbrashears/PycharmProjects/manim-cp/\""
    s = f" manim -q{q} "
    os.system("mkdir output")
    os.chdir(path)

    for i, x in enumerate(A):
        print(x)
        #s2 = f"{path}/{x}"
        os.system(f"{s}{x}")
        a = x[:-3]
        b = f"p{k(x)}"
        shutil.copyfile(f"{os.getcwd()}/media/videos/{a}/{qmap[q]}/{b}.mp4", f"{ROOT}/output/{a}.mp4")
        print(i, "---------->", a,"    ", b  )

    # input_video = ffmpeg.input('./output/0')
    # for x in input_video
