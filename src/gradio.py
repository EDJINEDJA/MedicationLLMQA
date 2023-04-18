import yaml
import argparse


from utils.utils import Dataloader , Functional


parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str , required=True ,  help='path to yaml config')
args = parser.parse_args()

with open(args.config, mode = 'r') as stream:
    config = yaml.safe_load(stream)


def greet(query):
    return Functional(config).QA_chroma("GPT4ALL",query)
