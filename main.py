from experiments import run_experiment, run_accuracy_experiment
import argparse
from pathlib import Path


# TODO: Add argparse for dataset path, experiment to run, etc
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path', help='Dataset path', default='./dataset/')

parser.add_argument('--prompt', help="Prompt to analyse",
                    default=None, nargs=2)

args = parser.parse_args()

if __name__ == '__main__':
    # arguments from parser
    dataset_path = args.dataset_path
    prompt = args.prompt

    if prompt is not None:
        run_experiment(prompt, dataset_path)

    else:
        run_accuracy_experiment(dataset_path)

    
