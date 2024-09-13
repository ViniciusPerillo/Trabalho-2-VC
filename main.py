import argparse
from pathlib import Path

from experiments import run_experiment, run_accuracy_experiment


def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dataset_path', help='Dataset path', default='./dataset/')
    parser.add_argument('--prompts', help="Prompt to analyze",
                        default=None, nargs=2)
    parser.add_argument('--seed', help="Number to seed randomized procedures (default: 1917)",
                        default=1917, metavar="N", type=int)

    return parser.parse_args()


if __name__ == '__main__':

    # Arguments from parser
    args = parse_args()

    dataset_path = Path(args.dataset_path)
    prompts = args.prompts
    random_seed = args.seed

    if prompts is not None:
        run_experiment(prompts, dataset_path, random_seed)

    else:
        run_accuracy_experiment(dataset_path)
