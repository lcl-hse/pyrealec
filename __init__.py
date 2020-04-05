# -*- coding: utf-8 -*-

import os
import shutil

import pandas as pd

from keras.utils import get_file


class RealecSubcorpus:
    def __init__(self, results, strategy="dataframe"):
        self.errors = []
        self.corrections = []

    def search(self, query):
        return RealecSubcorpus(results)

    def get_errors_by_type(self):
        return RealecSubcorpus(results)

    def filter(self, condition):
        return RealecSubcorpus(results)



class REALEC:
    
    def __init__(self, check=True, clean=True, filter_trees=["de"],
                 working_dir="~", filter_index=[], strategy="dataframe"):

        self.__working_dir = self._get_dir() or os.path.join(working_dir, "realec")

        if check:
            self._check_integrity(filter_trees=filter_trees)

        if clean:
            self._remove_trees(filter_trees)
            self.deduplicate()

        self.produce_index(filter_index)

        return RealecSubcorpus(corpus)

    def _get_dir(self):
        return realec_path

    def _check_integrity(self, filter_trees=[], restore_integrity=True):
        if ok:
            return True
        if restore_integrity:
            self.download()

    def _remove_trees(self, filter_trees):
        pass

    def download(self):
        pass

    def deduplicate(self):
        pass

    def produce_index(self, filter_index):
        pass

    def to_parallel(self):
        return parallel_df
