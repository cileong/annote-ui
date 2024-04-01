#!/usr/bin/env python3

import io
import sys
import os
import logging
import pprint
from pathlib import Path
from collections import defaultdict

from Main.models import *


def load_dataset(fp: io.TextIOBase) -> Dataset:
    data = f'{{ "annotations": {fp.read()} }}'
    return Dataset.model_validate_json(data)

def count_images(dataset: Dataset) -> int:
    return len(set(ann.image_filename for ann in dataset.annotations))

def count_instances(dataset: Dataset) -> int:
    return len(dataset.annotations)

def count_bbox_pairs(dataset: Dataset) -> int:
    return sum(len(ann.bbox_human) for ann in dataset.annotations)

def count_instances_by_class(dataset: Dataset) -> list[int]:
    cid2count = defaultdict(int)
    for ann in dataset.annotations:
        cid2count[ann.object_id] += 1

    n_classes = max(cid2count.keys()) + 1
    counter: list[int] = [0] * n_classes
    for cid, count in cid2count.items():
        counter[cid] += count

    return counter

def report_statistics(
        filename: str | os.PathLike,
        dataset: Dataset,
        logger: logging.Logger
    ) -> None:
    n_images = count_images(dataset)
    n_instances = count_instances(dataset)
    n_bbox_pairs = count_bbox_pairs(dataset)
    class_count = count_instances_by_class(dataset)

    report = f"""{Path(filename).name}
#images    : {n_images}
#instances : {n_instances}
#bboxpairs : {n_bbox_pairs}
{pprint.pformat(class_count)}
    """
    logger.info(report)

def main(args: list[str]) -> None:
    logger = logging.getLogger(name="counter")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    _, *dataset_filenames = args

    for filename in dataset_filenames:
        with Path(filename).open() as fp:
            dataset = load_dataset(fp)
        report_statistics(filename, dataset, logger)

if __name__ == "__main__":
    main(sys.argv)
