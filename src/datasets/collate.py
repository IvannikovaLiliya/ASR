import torch
from torch.nn.utils.rnn import pad_sequence


def collate_fn(dataset_items: list[dict]):
    """
    Collate and pad fields in the dataset items.
    Converts individual items into a batch.

    Args:
        dataset_items (list[dict]): list of objects from
            dataset.__getitem__.
    Returns:
        result_batch (dict[Tensor]): dict, containing batch-version
            of the tensors.
    """

    result_batch = {}
    
    result_batch["audio_path"] = [data_item["audio_path"] for data_item in dataset_items]
    result_batch["audio"] = [data_item["audio"] for data_item in dataset_items]
    result_batch["text"] = [data_item["text"] for data_item in dataset_items]

    result_batch["spectrogram"] = []    
    result_batch["spectrogram_length"] = torch.tensor(
        [data_item["spectrogram"].shape[2] for data_item in dataset_items])

    result_batch["text_encoded"] = []
    result_batch["text_encoded_length"] = torch.tensor(
        [data_item["text_encoded"].shape[1] for data_item in dataset_items])

    for data_item in dataset_items:
        result_batch["spectrogram"].append(data_item["spectrogram"].squeeze(0).T)
        result_batch["text_encoded"].append(data_item["text_encoded"].squeeze(0))

    result_batch["spectrogram"] = pad_sequence(result_batch["spectrogram"], batch_first=True).permute(0, 2, 1)
    result_batch["text_encoded"] = pad_sequence(result_batch["text_encoded"], batch_first=True)

    return result_batch