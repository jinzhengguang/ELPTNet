import os
import numpy as np

dirtrainval = [
    "bytes-cafe-2019-02-07_0",
    "clark-center-2019-02-28_0",
    "clark-center-2019-02-28_1",
    "clark-center-intersection-2019-02-28_0",
    "cubberly-auditorium-2019-04-22_0",
    "forbes-cafe-2019-01-22_0",
    "gates-159-group-meeting-2019-04-03_0",
    "gates-ai-lab-2019-02-08_0",
    "gates-basement-elevators-2019-01-17_1",
    "gates-to-clark-2019-02-28_1",
    "hewlett-packard-intersection-2019-01-24_0",
    "huang-2-2019-01-25_0",
    "huang-basement-2019-01-25_0",
    "huang-lane-2019-02-12_0",
    "jordan-hall-2019-04-22_0",
    "memorial-court-2019-03-16_0",
    "meyer-green-2019-03-16_0",
    "nvidia-aud-2019-04-18_0",
    "packard-poster-session-2019-03-20_0",
    "packard-poster-session-2019-03-20_1",
    "packard-poster-session-2019-03-20_2",
    "stlc-111-2019-04-19_0",
    "svl-meeting-gates-2-2019-04-08_0",
    "svl-meeting-gates-2-2019-04-08_1",
    "tressider-2019-03-16_0",
    "tressider-2019-03-16_1",
    "tressider-2019-04-26_2",
]
dirtest = [
    "cubberly-auditorium-2019-04-22_1",
    "discovery-walk-2019-02-28_0",
    "discovery-walk-2019-02-28_1",
    "food-trucks-2019-02-12_0",
    "gates-ai-lab-2019-04-17_0",
    "gates-basement-elevators-2019-01-17_0",
    "gates-foyer-2019-01-17_0",
    "gates-to-clark-2019-02-28_0",
    "hewlett-class-2019-01-23_0",
    "hewlett-class-2019-01-23_1",
    "huang-2-2019-01-25_1",
    "huang-intersection-2019-01-22_0",
    "indoor-coupa-cafe-2019-02-06_0",
    "lomita-serra-intersection-2019-01-30_0",
    "meyer-green-2019-03-16_1",
    "nvidia-aud-2019-01-25_0",
    "nvidia-aud-2019-04-18_1",
    "nvidia-aud-2019-04-18_2",
    "outdoor-coupa-cafe-2019-02-06_0",
    "quarry-road-2019-02-28_0",
    "serra-street-2019-01-30_0",
    "stlc-111-2019-04-19_1",
    "stlc-111-2019-04-19_2",
    "tressider-2019-03-16_2",
    "tressider-2019-04-26_0",
    "tressider-2019-04-26_1",
    "tressider-2019-04-26_3",
]

THRESH = 0.1
SUBMISSION_DIR = "data/e000040"
OUT_DIR = "data/detections"
print(OUT_DIR)

paths = os.listdir(SUBMISSION_DIR)
mymax = []
for i, path in enumerate(paths):
    print(f"process [{i}/{len(paths)}] {path}")
    seq_path = os.path.join(SUBMISSION_DIR, path)
    # 3d 跟踪
    if len(paths) == 7:
        seq_path_new = os.path.join(OUT_DIR, '{:04d}'.format(dirtrainval.index(path)))
    else:
        seq_path_new = os.path.join(OUT_DIR, '{:04d}'.format(dirtest.index(path)))
    os.makedirs(seq_path_new, exist_ok=True)

    for file in os.listdir(seq_path):
        det_path = os.path.join(seq_path, file)
        with open(det_path, "r") as f:
            lines = f.readlines()
        lines_new = []
        numx = 0
        for line in lines:
            datai = line.strip("\n").split(" ")
            if float(datai[-1]) > THRESH:
                linei = 'Pedestrian -1 -1 -1 -1 -1 -1 -1 {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                    float(datai[9]), float(datai[10]), float(datai[11]), float(datai[12]),
                    float(datai[13]), float(datai[14]), float(datai[15]), float(datai[16]))
                lines_new.append(linei)
            numx = numx + 1
        lines_new[-1] = lines_new[-1].strip('\n')
        mymax.append(len(lines_new))

        det_path_new = os.path.join(seq_path_new, file)
        with open(det_path_new, "w") as f:
            f.writelines(np.asarray(lines_new).tolist())

print('Pedestrian max: {}'.format(max(mymax)))

# 2025-03-10 Jinzheng Guang
