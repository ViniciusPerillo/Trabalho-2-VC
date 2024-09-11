from experiments import run_experiment, run_accuracy_experiment
import argparse
from pathlib import Path


# TODO: Add argparse for dataset path, experiment to run, etc
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path', help='Dataset path', default='./dataset/')

parser.add_argument('--prompt', help="Prompt to analyse",
                    default=None, nargs='+')
parser.add_argument('--experiment', help='bool to run experiment with a prompt',
                    default=False, type=bool)

args = parser.parse_args()

if __name__ == '__main__':
    # arguments from parser
    dataset_path = args.dataset_path
    prompt = args.prompt
    experiment = args.experiment

    if experiment and prompt is not None:
        run_experiment(prompt, dataset_path)

    elif experiment and prompt is None:
        raise Exception("Error, prompt parser is None, please insert a prompt")
    
    else:
        run_accuracy_experiment(dataset_path)

    
