import glob
import os
import shutil
import unittest

from pydd import pydd
from pydd.pydd import parse_args, set_logger_mode


class TestPydd(unittest.TestCase):
    def setUp(self):
        self.src = "init_test_dir"
        self.dst = "final_test_dir"
        os.makedirs(self.src, exist_ok=True)
        os.makedirs(self.dst, exist_ok=True)
        self.regex = "*.txt"

    def tearDown(self):
        if os.path.exists(self.src):
            shutil.rmtree(self.src)
        if os.path.exists(self.dst):
            shutil.rmtree(self.dst)

    def generate_fake_text_files(self, num_files: int):
        extension = "txt"
        for i in range(num_files):
            f = open(os.path.join(self.src, f"file{i}.{extension}"), "w")
            f.write(f"file {i} contents")
            f.close()

    def get_num_files_in_dir(self, dir: str):
        filenames = glob.glob(os.path.join(dir, self.regex))
        return len(filenames)

    def test_nothing_found(self):
        pydd(src_dir=self.src, dst_dir=self.dst, regex=self.regex)

    def test_pydd(self):
        set_logger_mode(quiet_mode=False)
        num_files = 10
        self.generate_fake_text_files(num_files)
        self.assertEqual(self.get_num_files_in_dir(self.src), num_files)
        pydd(
            src_dir=self.src,
            dst_dir=self.dst,
            regex=self.regex,
            disable_progressbar=False,
        )
        self.assertEqual(self.get_num_files_in_dir(self.dst), num_files)
        self.assertEqual(self.get_num_files_in_dir(self.src), 0)

    def test_logger_setup(self):
        set_logger_mode(quiet_mode=True)
        set_logger_mode(quiet_mode=False)

    def test_parse_args(self):
        parser = parse_args(
            ["--src", self.src, "--dst", self.dst, "--regex", self.regex]
        )
        self.assertEqual(parser.src, self.src)
        self.assertEqual(parser.quiet, False)


if __name__ == "__main__":
    unittest.main()
