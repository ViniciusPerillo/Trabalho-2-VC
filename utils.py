import warnings
from pathlib import Path

from torchvision.datasets import OxfordIIITPet
from transformers import CLIPProcessor, CLIPModel
from numpy.random import default_rng
from torch import cuda
from tqdm import tqdm

warnings.filterwarnings('ignore')


DEVICE = "cuda:0" if cuda.is_available() else "cpu"

def load_dataset(path: Path = Path('./dataset/'), target_type: str = 'binary-category'):
    ds = OxfordIIITPet(root=path, split='test', target_types=target_type, download=True)
    return ds

def load_processor():
    processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')
    return processor

def load_model():
    model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
    return model.to(DEVICE)


def run_model(processor: CLIPProcessor,
              model: CLIPModel,
              images: list,
              prompts: list):

    if not isinstance(images, list) or not isinstance(prompts, list):
        raise ValueError("`images` and `prompts` should be `list`s")
    
    input = processor(text=prompts, images=images, return_tensors='pt', padding=True).to(DEVICE)
    output = model(**input)

    return output


def sample_equally(dataset: OxfordIIITPet, n_images_each: int = 1000, random_seed: int = 1917):
    cats = []
    dogs = []

    idxs = list(range(len(dataset)))
    default_rng(random_seed).shuffle(idxs)

    for idx in tqdm(idxs, desc="Sampling images"):
        image, label = dataset[idx]
        
        if len(cats) == n_images_each and len(dogs) == n_images_each:
            break

        if len(cats) < n_images_each and label == 0:           # cat
            cats.append(image)
        elif len(dogs) < n_images_each and label == 1:         # dog
            dogs.append(image)


    print('Successfully sampled!')
    return cats + dogs

def batch_images(images: list, batch_size: int = 50):
    if len(images) % batch_size != 0:
        raise NotImplementedError("The number of images must be a multiple of `batch_size`")

    for i in range(0, len(images), batch_size):
        yield images[i : i + batch_size]
