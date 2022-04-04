en = "/home/toni/repos/npfl120/hw05-pos-tagging/data/en.s"
ru = "/home/toni/repos/npfl120/hw05-pos-tagging/data/ru.s"
tr = "/home/toni/repos/npfl120/hw05-pos-tagging/data/tr.s"
kk = "/home/toni/repos/npfl120/hw05-pos-tagging/data/kk.s"

with open(en) as en_file, open(ru) as ru_file, open(tr) as tr_file, open(kk) as kk_file, open(en + ".mod", "w") as en_out, open(ru + ".mod", "w") as ru_out, open(tr + ".mod", "w") as tr_out, open(kk + ".mod", "w") as kk_out:
    for i in range(149605):
        en_line = en_file.readline().strip()
        ru_line = ru_file.readline().strip()
        tr_line = tr_file.readline().strip()
        kk_line = kk_file.readline().strip()

        if en_line == "" or len(en_line) == 0:
            continue
        
        if ru_line == "" or len(ru_line) == 0:
            continue

        if tr_line == "" or len(tr_line) == 0:
            continue
        
        if kk_line == "" or len(kk_line) == 0:
            continue
        
        en_out.write(en_line + "\n")
        ru_out.write(ru_line + "\n")
        tr_out.write(tr_line + "\n")
        kk_out.write(kk_line + "\n")