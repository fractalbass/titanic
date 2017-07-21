import pandas as pd


class FileUtils:

    def __init__(self, **kwargs):
        self.filename = kwargs['filename']
        self.skip_header = kwargs.get('skip_header', True)
        self.whitespace_delim = kwargs.get('whitespace_delim', False)

    def get_arrays_from_csv(self):
        df = pd.read_csv(self.filename, header=None, delim_whitespace=self.whitespace_delim)
        all_rows = []
        for idx, row in df.iterrows():
            if idx == 0:
                if not self.skip_header:
                    all_rows.append([float(i) for i in row.tolist()])
            else:
                all_rows.append([float(i) for i in row.tolist()])
        return all_rows

