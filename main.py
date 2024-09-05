import numpy as np

from utils import *
from plots import *
from scipy.spatial.distance import cosine


# TODO: Batch images?  --  should work normally due to np.stack
# TODO: Add GPU support


if __name__ == '__main__':
    
    # Loading dataset, CLIP pre-processor and CLIP model
    ds = load_dataset()
    processor = load_processor()
    model = load_model()


    # Sampling 1000 images of cats and dogs (cats come first)
    images = sample_equally(ds)


    # Prompts to use with CLIP
    prompts = [
        'Cat',
        'Dog',
    ]


    # Running model and saving necessary information
    logits_image = []
    logits_text  = []

    embeds_image = []
    embeds_text  = None

    for img in tqdm(images, desc="Processing images"):
        output = run_model(processor, model, [img], prompts)

        logits_image.append( output.logits_per_image.cpu().detach().numpy() )
        logits_text.append(  output.logits_per_text.cpu().detach().numpy()  )

        embeds_image.append( output.image_embeds.cpu().detach().numpy()     )

        # Since the texts are the same, their embeddings are also the same
        if embeds_text is None:
            embeds_text = output.text_embeds.cpu().detach().numpy()


    logits_image = np.stack(logits_image, axis=0)
    logits_text  = np.stack(logits_text, axis=0)

    embeds_image = np.stack(embeds_image, axis=0).squeeze()


    print(f'{logits_image.shape=}')
    print(f'{logits_text.shape=}')

    print(f'{embeds_image.shape=}')
    print(f'{embeds_text.shape=}')


    # Calculating cosine similarity between images and texts embeddings

    # Defining cat and dog indexes for better readability
    CAT_IDX = 0
    DOG_IDX = 1

    similarities = {
        "Cat": [ cosine(img, embeds_text[CAT_IDX]) for img in embeds_image ],
        "Dog": [ cosine(img, embeds_text[DOG_IDX]) for img in embeds_image ]
    }

    plot_similarities_histogram(similarities)

    plot_similarities_scatter(similarities)
