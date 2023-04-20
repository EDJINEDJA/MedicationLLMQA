import yaml
import argparse


from utils.utils import Dataloader , Functional


parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str , required=True ,  help='path to yaml config')
args = parser.parse_args()

with open(args.config, mode = 'r') as stream:
    config = yaml.safe_load(stream)


def app(query:str)-> object:
    """_summary_

    Args:
        query (_type_=str): _description_=It is the input text, it can be a question

    Returns:
        _type_=str: _description_ = This is the output, it is the response according to the question asked before
    """
    return Functional(config).QA_faiss(query)
