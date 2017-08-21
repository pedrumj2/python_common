class File_IO:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_all_lines(self):
        output = []
        with open(self.file_path) as f:
            for line in f:
                output.append(line.rstrip("\n"))
        return output

    def csv_read__all_lines(self):
        output = []
        lines = self.read_all_lines()
        for i in range(len(lines)):
            line = lines[i].split(",")
            output.append(line)
        return output

    def csv_print(self, lines):
        f = open(self.file_path, 'w')
        for i in range(len(lines)):
            line = ""
            for j in range(len(lines[i])-1):
                line += lines[i][j] + ","
            line += lines[i][len(lines[i])-1] + "\n"
            f.write(line)
        f.close()  # you can omit

