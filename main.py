import argparse
from pathlib import Path

from experiments import run_experiment, run_accuracy_experiment


def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dataset_path', help='Dataset path', default='./dataset/')
    parser.add_argument('--prompts', help="Prompt to analyse",
                        default=None, nargs=2)

    return parser.parse_args()


if __name__ == '__main__':

    # Arguments from parser
    args = parse_args()

    dataset_path = Path(args.dataset_path)
    prompts = args.prompts

    if prompts is not None:
        run_experiment(prompts, dataset_path)

    else:
        run_accuracy_experiment(dataset_path)
