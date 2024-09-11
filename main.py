from experiments import run_experiment, run_accuracy_experiment
import argparse
from pathlib import Path


# TODO: Add argparse for dataset path, experiment to run, etc
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path', help='Dataset path', default='./dataset/')
parser.add_argument('--download_dataset', help="Bool to download dataset",
                    default=False, type=bool)
parser.add_argument('--prompt', help="Prompt to analyse",
                    default=None, nargs='+')
parser.add_argument('--experiment', help='bool to run experiment with a prompt',
                    default=False, type=bool)

args = parser.parse_args()

if __name__ == '__main__':

    # prompts = [
    #     "Cat",
    #     "Dog"
    # ]

    # prompts = [
    #     "A photo of a cat",
    #     "A photo of a dog"
    # ]

    # prompts = [
    #     "A photo of a cat, a type of pet",
    #     "A photo of a dog, a type of pet"
    # ]

    # run_experiment(prompts)
    
    dataset_path = args.dataset_path
    download_dataset = args.download_dataset
    prompt = args.prompt
    experiment = args.experiment

    if experiment and prompt is not None:
        run_experiment(prompt, dataset_path, download_dataset)
    elif experiment and prompt is None:
        raise Exception("Error, prompt parser is None, please insert a prompt")
    else:
        run_accuracy_experiment(dataset_path, download_dataset)

    
