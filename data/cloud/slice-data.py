import os

path = "logs"
for f in os.listdir(path):
    file_path = os.path.join(path, f)
    file_num = f[4::]

    a_count = 0
    b_count = 0

    with open(file_path) as f:
        for line in f:
            if "Measurement A" in line:
                break
        else:
            raise RuntimeError("Failed to find Measurement A in %s" % f)

        with open("bench_%s_A" % file_num, "w") as bench_a:
            for line in f:
                if "Measurement B" in line:
                    break
                if line.startswith("test"):
                    a_count += 1
                    bench_a.write(line)
            else:
                raise RuntimeError("Failed to find Measurement B in %s" % f)
        
        with open("bench_%s_B" % file_num, "w") as bench_b:
            for line in f:
                if line.startswith("test"):
                    b_count += 1
                    bench_b.write(line)

        print "%s: A: %d, B: %d" % (file_path, a_count, b_count)
