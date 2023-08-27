# Elder Speech Generator
This project aims to generate sentences in Elder Speech, the main language of elves and dryads in the Witcher universe. Elder Speech is based on Celtic languages, but also has influences from other languages like Italian and Latin. It is spoken by elves, mages, scholars, dryads, sirens, and nereids.

## Model Description
The model is a non-pretrained embedding layer and two-layer bidirectional LSTM with 128 units. The model has a vocabulary of around 380 words, which were scraped from [Witchers fandom](https://witcher.fandom.com/wiki/Elder_Speech) along with their English translations. I put together over 50 sentences that were used for training and it took more time than I expected. The model was trained for 200 epochs.

## Dataset download
If you would like to download only the data without the translations or sentences I published everything on [Kaggle](https://www.kaggle.com/datasets/kacperrabczewski/witcher-elder-speech?select=sentences.csv).

## Model Output
The model can generate sentences in Elder Speech that are somewhat grammatically correct and meaningful. The sentences are sampled from the probability distribution of a softmax layer. Here are some examples of what the model can generate and their translations:

| Generated text | Translation |
|---|---|
| Gwynbleidd ess y vatt'ghern ui aesledde aen an evall. | The white wolf is of witcher and rides on a horse. |
| Iade y twe tir ess an uniade y treise. |	Of two country is an merger of power. |
| Av’caaren meath aen mid y pont an egweth. |	Meet as in the middle of a bridge. |
